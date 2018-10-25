import pika

node = pika.URLParameters('amqp://yuwei:openstack@10.50.0.82:5672/')
connection = pika.BlockingConnection(node)
channel = connection.channel()
channel.queue_declare(queue='hello')

channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World!')
print " [x] Sent 'Hello World!'"

connection.close()

