#!/usr/bin/env python
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='hello_queue', durable=True) # To declare/create the queue, if not happened before


for x in range(10):
    # TODO: Please send a *durable* message into the queue hello_queue.
    # The body (content) of the messages should be 'Message number: ' + str(x) 
    print(" [x] Sent 'Message: " + str(x) + "'")

print("Send ended")

connection.close()