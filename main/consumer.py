import pika
import time
import json
from main import Product, db

params = pika.URLParameters('amqp://guest:guest@queue:5672/')

while True:
    try:
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        break 
    except pika.exceptions.AMQPConnectionError:
        print("RabbitMQ not ready yet. Retrying in 5 seconds...")
        time.sleep(5)

channel.queue_declare(queue='main')

def callback(ch, method, properties, body):
    print('Received in main')
    data = json.loads(body)
    print(data)


channel.basic_consume(queue='main', on_message_callback=callback, auto_ack=True)

print('Started Consuming')
channel.start_consuming()