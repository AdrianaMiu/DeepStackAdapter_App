import pika


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
   

data_retriver = RabbitDataHandler()
metadata = data_retriver.get_data('Input') #one single message from queue

