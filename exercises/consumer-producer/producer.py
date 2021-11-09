#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='msg_queue', durable=True) # Channel = Durable


for x in range(10):
    channel.basic_publish(exchange='',
                        routing_key='msg_queue',
                        body='Message number: ' + str(x),
                        properties=pika.BasicProperties(
                         delivery_mode = 2, #Message = Persistent
                      ))
    print(" [x] Sent 'Message: '" + str(x))

print("Send ended")

connection.close()