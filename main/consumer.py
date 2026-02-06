

import pika

params = pika.URLParameters('amqp://guest:guest@queue:5672/')

connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='main')
def callback(ch, method,properties,body):
    print('main has recieved')
    print(body)

channel.basic_consume(queue='main',on_message_callback=callback)

print ('Consuming has begun')
channel.start_consuming()
channel.close()