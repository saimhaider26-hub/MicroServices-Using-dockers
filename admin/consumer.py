

import pika

params = pika.URLParameters('amqp://guest:guest@queue:5672/')

connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='admin')
def callback(ch, method,properties,body):
    print('admin has recieved')
    print(body)

channel.basic_consume(queue='admin',on_message_callback=callback,auto_ack=True)

print ('Consuming has begun')
channel.start_consuming()
channel.close()