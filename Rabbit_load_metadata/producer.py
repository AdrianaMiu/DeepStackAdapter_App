import pika
import json
import sys
import os

#credentials = pika.PlainCredentials('guest', 'guest')
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

file_path = os.path.join(os.getcwd(), 'rabbit_msg.json')
json_data = json.load(open(file_path))
channel = connection.channel()

#declare a queue
channel.queue_declare(queue= 'Input')

for i in range(int(sys.argv[1])):
    channel.basic_publish(exchange='', routing_key='Input', body=json.dumps(json_data))
    print(f"Sent message {i}")
channel.close()