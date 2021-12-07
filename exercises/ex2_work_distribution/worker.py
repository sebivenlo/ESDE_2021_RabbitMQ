#!/usr/bin/env python
import pika, sys, os, time
from datetime import datetime
import json

def process_task(task):
    # TODO: Implement the process_task function
    # This should: 
    # - Convert the task-string into a object (by using the json library)
    # - Parse the date attribute from the object into a date object (see: datetime.fromtimestamp)
    # - Return afterwards a string like this derived from the task:
    # "Message - Date: 2021-12-07 16:18:13.662463"
    return "TODO"

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()
    channel.exchange_declare(exchange='work_abc', exchange_type='fanout')
    channel.queue_declare(queue='work_queue_1')

    

    def callback(ch, method, properties, body):
        print("_________________________________________________________________")
        print(" [☛] Task received %r" % body.decode())
        print(" [☛] Task processed. Result: %r" % process_task(body.decode()))
        print("_________________________________________________________________")

    channel.basic_consume(
        #TODO: Make sure that the work_queue_1 is consumed
        on_message_callback=callback,
        auto_ack=True
        )

    print(' [☛] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)