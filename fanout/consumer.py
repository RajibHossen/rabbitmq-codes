import pika
import time


connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',type='fanout')

channel.queue_declare(queue='account_logs',exclusive=True)

channel.queue_bind(exchange='logs',queue='account_logs')

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(callback,queue='account_logs')

print(' [*] Account Queue \n Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
