import pika, sys

from pika import spec

credentials = pika.PlainCredentials("ipvision", "ipvision123")
conn_params = pika.ConnectionParameters('192.168.122.198',5672,'/',credentials)
conn_broker = pika.BlockingConnection(conn_params)
channel = conn_broker.channel()

channel.exchange_declare(exchange='hello-exchange',type='direct')

def callback(frame):
    if type(frame.method) == spec.Confirm.SelectOk:
        print "Channel in 'confirm' mode."
    elif type(frame.method) == spec.Basic.Nack:
        if frame.method.delivery_tag in msg_ids:
            print "Message lost!"
    elif type(frame.method) == spec.Basic.Ack:
        if frame.method.delivery_tag in msg_ids:
            print "Confirm received!"
            msg_ids.remove(frame.method.delivery_tag)

channel.confirm_delivery()

msg_props = pika.BasicProperties()
msg_props.content_type = "text/plain"
msg_ids = []
if channel.basic_publish(body="helllloo",exchange="hello-exchange",properties=msg_props,routing_key="hola"):
    print "confirm"
else:
    print "fail"
msg_ids.append(len(msg_ids) + 1)

channel.close()
