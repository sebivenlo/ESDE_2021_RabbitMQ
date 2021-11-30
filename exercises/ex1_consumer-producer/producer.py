#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello_queue', durable=True) # To declare/create the queue, if not happened before


for x in range(10):
    channel.basic_publish(
                            exchange='',
                            routing_key='hello_queue',
                            body='Message number: ' + str(x),
                            properties=pika.BasicProperties(
                                delivery_mode = 1,
                            )
                        )
    print(" [x] Sent 'Message: " + str(x) + "'")

print("Send ended")

connection.close()