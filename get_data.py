import pika
import json


class RabbitDataHandler():
    def __init__(self, host='localhost'):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
        self.channel = self.connection.channel()
    
    def get_data(self, queue_name):
        self.channel.queue_declare(queue=queue_name)
        method_frame, header_frame, body = self.channel.basic_get(queue_name)
        # Check if there was a message in the queue
        if method_frame:
            self.channel.basic_ack(method_frame.delivery_tag)
            
            return body
        else:
            #no message wa retrieved
            return None
   
    def write_data(self, queue_name, message):
        self.channel.queue_declare(queue=queue_name)
        self.channel.basic_publish(exchange='', routing_key=queue_name, body=message,
                                    properties=pika.BasicProperties(delivery_mode=2))
    def close(self):
        # Close the connection
        self.connection.close()


data_retriver = RabbitDataHandler()

    