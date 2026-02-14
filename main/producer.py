import pika, json

def publish(method, body):
    params = pika.URLParameters('amqp://guest:guest@queue:5672/')

    try:
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        
        properties = pika.BasicProperties(content_type=method)
        channel.basic_publish(
            exchange='',
            routing_key='admin', 
            body=json.dumps(body),
            properties=properties
        )
        
        print(f'DEBUG: Sent {method} to queue for admin')
        connection.close()

    except Exception as e:
        print(f'error')