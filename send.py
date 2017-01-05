#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('rajib', 'rajib')
parameters = pika.ConnectionParameters('192.168.122.75', 5672, '/', credentials)
connection = pika.BlockingConnection(parameters)

channel = connection.channel()

channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',routing_key='hello',body='Hello World!')
print(" [x] sent Hello World!")

connection.close()
