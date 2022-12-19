import pika
import sys
import os

def main():
    #connect to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    #declare a queue
    channel.queue_declare(queue='Input')

    #callback function to process the message
    def callback(ch, method, properties, body):
        print(f'Received data: {body}')

    #consume messages
    channel.basic_consume(queue='Input', on_message_callback=callback, auto_ack=True)

    #consumer loop
    print("Messages:")
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except:
            os._exit(0)