#!/usr/bin/env python
import pika
import json
import time
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='work_exchange', exchange_type='fanout')
queue = channel.queue_declare(queue='work_queue_1')
channel.queue_bind(queue=queue.method.queue, exchange='work_exchange')

data = {'date': time.time(), 'message': ' '.join(sys.argv[1:]) or "Hello World!"}

channel.basic_publish(exchange='work_exchange',
                      routing_key='',
                      body=json.dumps(data))
print(" [☛] Sent %r" % data)


connection.close()