from flask import Flask, jsonify, abort
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy  
from sqlalchemy import UniqueConstraint
from dataclasses import dataclass
import requests
from producer import publish

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:root@db_main/main'
CORS(app)

db = SQLAlchemy(app)  


@dataclass
class Product(db.Model):
    id: int 
    title: str 
    image: str
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    title = db.Column(db.String(200))
    image = db.Column(db.String(200))

@dataclass
class ProductUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)

    __table_args__ = (
        UniqueConstraint('user_id', 'product_id', name='user_product_unique'),
    )
@app.route('/api/products')
def index():
    products = Product.query.all()
    return jsonify([
        {'id': p.id, 'title': p.title, 'image': p.image} 
        for p in products
    ])

@app.route('/api/products/<int:id>/like', methods=['POST'])
def like(id):
    try:
        req = requests.get('http://admin:8000/api/user')
        req_json = req.json() 
    except Exception:
        return jsonify({"message": "Admin service is unreachable or sent invalid data"}), 400

    try:
        productUser = ProductUser(user_id=req_json['id'], product_id=id)
        db.session.add(productUser)
        db.session.commit()
        publish('product_liked', id)
      
    except:
        abort(400, 'You already liked this product')

    return jsonify({'message': 'success'})


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
    