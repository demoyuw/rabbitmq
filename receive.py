import pika

node = pika.URLParameters('amqp://yuwei:openstack@10.50.0.82:5672/')
connection = pika.BlockingConnection(node)
channel = connection.channel()

channel.queue_declare(queue='hello')

print ' [*] Waiting for messages. To exit press CTRL+C'

def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)

channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)

channel.start_consuming()
connection.close()
