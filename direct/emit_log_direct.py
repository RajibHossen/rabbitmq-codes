#!/usr/bin/env python
import pika
import sys

credential = pika.PlainCredentials("ipvision","ipvision123")
conn_params = pika.ConnectionParameters('192.168.122.198',5672,'/',credential)

connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Hello World!'
channel.basic_publish(exchange='direct_logs',
                      routing_key=severity,
                      body=message)
print(" [x] Sent %r:%r" % (severity, message))
connection.close()
