import pika
import time


connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs',type='fanout')

result = channel.queue_declare(queue='hack_logs',exclusive=True)

queue_name = result.method.queue

channel.queue_bind(exchange='logs',queue=queue_name)

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


channel.basic_consume(callback,queue=queue_name)

print(' [*] QUEUE-hack_logs...\nWaiting for messages. To exit press CTRL+C')
channel.start_consuming()
