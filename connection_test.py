import sys, pika

EXIT_OK = 0
EXIT_WARNING = 1
EXIT_CRITICAL = 2
EXIT_UNKNOWN = 3

server = sys.argv[1]
port = int(sys.argv[2])
vhost = sys.argv[3]
username = sys.argv[4]
password = sys.argv[5]

creds_broker = pika.PlainCredentials(username, password)
conn_params = pika.ConnectionParameters(server,port,vhost,creds_broker)

try:
    conn_broker = pika.BlockingConnection(conn_params)
    channel = conn_broker.channel()
except Exception:
    print "CRITICAL: Could not connect to %s:%s!" % (server, port)
    exit(EXIT_CRITICAL)
print "OK: Connect to %s:%s successful." % (server, port)
exit(EXIT_OK)
