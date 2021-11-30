#!/usr/bin/env python
import pika
import sys
from datetime import datetime

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='work_queue', durable=True)  # To declare/create the queue, if not happened before


message = ' '.join(sys.argv[1:]) or "Hello World! - " + datetime.now().strftime("%H:%M:%S")
channel.basic_publish(exchange='',
                      routing_key='work_queue',
                      body=message)
print(" [☛] Sent %r" % message)


connection.close()