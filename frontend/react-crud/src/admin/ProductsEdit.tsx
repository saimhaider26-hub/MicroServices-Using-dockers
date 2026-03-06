import React, { SyntheticEvent, useState, useEffect } from 'react';
import Wrapper from "./Wrapper";
import { useNavigate, useParams } from 'react-router-dom';

const ProductsEdit = () => {
    const [title, setTitle] = useState('');
    const [image, setImage] = useState('');
    const navigate = useNavigate();
    const { id } = useParams();

    useEffect(() => {
        (async () => {
            const response = await fetch(`http://localhost:8000/api/products/${id}`);
            const product = await response.json();
            setTitle(product.title);
            setImage(product.image);
        })();
    }, [id]);

    const submit = async (e: SyntheticEvent) => {
        e.preventDefault();

        await fetch(`http://localhost:8000/api/products/${id}`, {
            method: 'PUT',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                title,
                image
            })
        });

        navigate('/admin/products');
    }

    return (
        <Wrapper>
            <form onSubmit={submit}>
                <div className="form-group">
                    <label>Title</label>
                    <input type="text" className="form-control" name="title"
                           defaultValue={title}
                           onChange={e => setTitle(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label>Image</label>
                    <input type="text" className="form-control" name="image"
                           defaultValue={image}
                           onChange={e => setImage(e.target.value)}
                    />
                </div>
                <button className="btn btn-outline-secondary">Save</button>
            </form>
        </Wrapper>
    );
};

export default ProductsEdit;