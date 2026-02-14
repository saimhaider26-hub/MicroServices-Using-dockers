import pika, json, os, django, time
from django.db import connections

time.sleep(13)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product 

params = pika.URLParameters('amqp://guest:guest@queue:5672/')
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('flask message to admin')
    
    connections.close_all()
    
    product_id = json.loads(body)
    print(f'product with id {product_id} has been updated')
    
    try:
        product = Product.objects.get(id=product_id)
        product.likes = product.likes + 1
        product.save()
        print(f'Likes increased for {product.title}')
    except Product.DoesNotExist:
        print(f'Error: Product {product_id} isnt in admin db')
    except Exception as e:
        print(f'error')

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Consuming started')
channel.start_consuming()