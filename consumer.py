#!/usr/bin/env python
import pika
import sys

credentials = pika.PlainCredentials("ipvision", "ipvision123")
conn_params = pika.ConnectionParameters('192.168.122.198',5672,'/',credentials)
conn_broker = pika.BlockingConnection(conn_params)
channel = conn_broker.channel()

channel.exchange_declare(exchange='hello-exchange',
                         type='direct')

result = channel.queue_declare(exclusive=True)
queue_name = result.method.queue

channel.queue_bind(exchange='hello-exchange',queue=queue_name,routing_key='hola')

print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r:%r" % (method.routing_key, body))

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()

