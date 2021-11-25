## Prerequisites
In order to run the scripts and the RabbitMQ broker, please follow the instructions below.
1. Install docker
https://www.docker.com/products/docker-desktop

2. Install python
https://www.python.org/about/gettingstarted/

3. Install the pika library for python (command line)
```
python -m pip install pika --upgrade
```

## Getting started 

To start the message broker, simply execute the following command in the console. 
```
docker-compose up
```

After the docker container has pulled the rabbitmq image, you can check whether the docker container runs by visiting the following website:
[RabbitMQ Management UI](http://127.0.0.1:15672/)

The default user credentials for this web interface are as follows:
```
username: guest
password: guest
```


[← Previous chapter](presentation/index.html) | [Back to start page](index.md) | [Next chapter →](exercises.md)