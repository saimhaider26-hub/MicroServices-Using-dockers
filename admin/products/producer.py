import pika

def publish():
    print('DEBUG: Starting publish function...')
    
    params = pika.URLParameters('amqp://guest:guest@queue:5672/')
    print('DEBUG: URL parameters set.')

   
    try:
        connection = pika.BlockingConnection(params)
        print('DEBUG: Connection successful!')
    except Exception as e:
        print(f'DEBUG: CRASHED during connection: {e}')
        return

    try:
        channel = connection.channel()
        print('DEBUG: Channel created.')
    except Exception as e:
        print(f'DEBUG: CRASHED during channel creation: {e}')
        return

   
    try:
        channel.basic_publish(exchange='', routing_key='main', body='hello')
        print('DEBUG: Message published!')
    except Exception as e:
        print(f'DEBUG: CRASHED during publish: {e}')
        return
    

    connection.close()
    print('DEBUG: Connection closed. Done.')
