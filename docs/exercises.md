# Exercises

## 1. Explore the RabbitMQ web interface

As mentioned before, together with the docker-container, a web interface has been set up by RabbitMQ. This can be accessed by clicking on the following link:

[RabbitMQ Management UI](http://127.0.0.1:15672/)

The default user credentials for this web interface are as follows:
```
username: guest
password: guest
```

The first exercise is to study the web interface a bit. There is no specific goal set for this exercise, so just explore for *1-5 minutes*.

## 2. Send durable messages

The first exercise is used to get familiar with the environment and in particular specialties of RabbitMQ. Therefore, go into the folder ```exercises/ex1_consumer-producer/```. You'll find two python files:
1. consumer.py &rarr; Consumes the message queue
1. producer.py &rarr; Produces messages into the message queue


**_Your task:_**
```
The developer of the message queue has created the python producer in a way that messages are lost when the message broker (here: docker-container) restarts.
Suddenly, the code for sending the messages into the queue was lost 
(someone forgot to commit).

Can you implement the producer in a way so that messages are sent durable to the corresponding queue?
```
**_To check that the messages are not lost and your task is completed, perform the following operations:_**

1. Run the producer: ```python producer.py```
1. Stop the producer with <kbd>Ctrl</kbd> + <kbd>C</kbd>
1. Stop docker container with <kbd>Ctrl</kbd> + <kbd>C</kbd>
1. Start docker container again with ```docker-compose up```
1. Run the consumer: ```python consumer.py```

*Execute the <kbd>Ctrl</kbd> + <kbd>C</kbd> hotkey in the terminal where the program runs (e.g. producer)*

The exercise is finished, when after performing the above steps the messages from the producer are received by the consumer whicch have been sent *before* the restart of the message broker (docker container).

[← Previous chapter](getting_started.md) | [Back to start page](index.md) | [Next chapter →](quiz.md)

## 3. Message interpretation 

The second exercise is used to get familiar with work distrubution in RabbitMQ and to first let the worker do "real" work. Therefore, go into the folder ```exercises/ex2_work_distribution/```. You'll find two python files:
1. work_distributor.py &rarr; Produces work (tasks) for the worker
1. worker.py &rarr; Gets a task from the work_distrubutor and processes it

**_Your task:_**
```
The company you are asked for to develop this piece of software wants to send messages and the timestamp to an exchange. This exchange is routed to the queue. Your task is to develop the worker.py, so it receives the message from the correct queue.
Besides that, you have to implement the process_task(task) function, which should load the JSON-string into a python object and print return (depending on the task) a string like this:

"Message - Date: 2021-12-07 16:18:13.662463"

```