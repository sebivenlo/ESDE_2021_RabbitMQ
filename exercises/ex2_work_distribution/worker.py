#!/usr/bin/env python
import pika, sys, os, time

def process_task(task):
    return task

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='work_queue', durable=True)  # To declare/create the queue, if not happened before

    def callback(ch, method, properties, body):
        print(" [☛] Task received %r" % body.decode())
        print(" [☛] Task processed. Result: %r" % process_task(body.decode()))
        time.sleep(body.count(b'.'))
        print(" [☛] Done")

    channel.basic_consume(queue='work_queue', on_message_callback=callback, auto_ack=True)

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