import pika, sys, os
import time

# Step 1: create a connection with a broker on Rabbit MQ server
# Here "localhost" is address of server. It could have been IP instead.
# The address: "localhost" will only work if RabbitMQ server is running on your local machine.


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))

    # Step 2 : open/create a channel.
    channel = connection.channel()

    channel.queue_declare("hello")
    # INFO: We tried to call the queue creation statement again,
    # since we just want to be sure that it exists.
    # it's a good practice to repeat declaring the queue in both programs.

    # *********** Receiving messages **************
    # we receive by subscribing a callback function to a queue.
    ## That exactly like, reacting to a new event.  In this case, a message arriving in a queue.

    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode()}")
        time.sleep(body.count(b"."))
        print(" [x] Done")

    # Tell RMQ that above callback function will receive messages from our "hello" queue.
    channel.basic_consume(queue="hello", auto_ack=True, on_message_callback=callback)

    # *** Start a never ending listener that would listen for messages *********
    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
