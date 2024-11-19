#!/usr/bin/env python
# Note: Install these things before you start:
# Erlang OTP (v 27) from https://www.erlang.org/downloads
# Download rabbbit mq installer: https://github.com/rabbitmq/rabbitmq-server/releases/download/
# Also on windows, add the path to environ PATH (e.g) >
# C:\Program Files\RabbitMQ Server\rabbitmq_server-4.0.3\sbin

# Starting RabbitMQ on windows machine
# rabbitmq-service.bat start & if not errorlevel 1 exit /b 0

import pika

# Step 1: create a connection with a broker on Rabbit MQ server
# Here "localhost" is address of server. It could have been IP instead.
# The address: "localhost" will only work if RabbitMQ server is running on your local machine.
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

# Step 2 : open/create a channel.
channel = connection.channel()

# Queues: We deliver messages using queues.
# Step 3: Create a queue that will be used to send a message.
channel.queue_declare("hello")
# Note: This is a NAMED queue.
# Note: Now if you execute any more, it will not create the same queue anymore.

# Test 1:
# Send a message using the queue.

### *** IMP NOTE: ***
# In RabbitMQ, a message CANNOT be directly SENT to a queue.
# It ALWAYS NEED to go through an EXCHANGE

## INFO: A default exchange IS an EMPTY string. e.g exchange=""
# This exchange is special ‒ it allows us to specify exactly to which queue the message should go.
# Below code explination:
# exchange: "" (Default)
# routing_key: name of queue
# body: the message to be sent.
channel.basic_publish(exchange="", routing_key="hello", body="Hello dear")
print(" [x] Sent 'Hello World!'")

# after sending the message, close the connection.
connection.close()
