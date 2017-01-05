import pika, json, time

creds_broker = pika.PlainCredentials("rajib", "rajib")
conn_params = pika.ConnectionParameters('192.168.122.75',5672,'/',creds_broker)
conn_broker = pika.BlockingConnection(conn_params)
channel = conn_broker.channel()

channel.exchange_declare(exchange="rpc",type="direct",auto_delete=False)
channel.queue_declare(queue="ping", auto_delete=False)
channel.queue_bind(queue="ping",exchange="rpc",routing_key="ping")

def api_ping(channel, method, header, body):
    """'ping' API call."""
    channel.basic_ack(delivery_tag=method.delivery_tag)
    msg_dict = json.loads(body)
    print "Received API call...replying..."
    time.sleep(5)
    channel.basic_publish(body="Pong!" + str(msg_dict["time"]),exchange="",routing_key=header.reply_to)
    print "Replied to client with success. see in client program"

channel.basic_consume(api_ping,queue="ping",consumer_tag="ping")

print "Waiting for RPC calls..."

channel.start_consuming()
