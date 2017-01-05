#!/usr/bin/env python
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='task_queue_2',durable=True)

message = ' '.join(sys.argv[1:]) or "Hello World!"

channel.basic_publish(exchange='',routing_key='task_queue_2',body=message, 
	properties = pika.BasicProperties(delivery_mode=2,))

print(" [x] sent %r" % message)

connection.close()


