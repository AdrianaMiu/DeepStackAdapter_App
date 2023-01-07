from get_images import *
from get_data import *
from get_prediction import *

#objects
data_retrieve = RabbitDataHandler()
image_retrieve = RedisReader()
predictor = DeepStackClient()

#retrieve data and image
metadata = data_retrieve.get_data('Input') 
image_data = image_retrieve.get_images("dog.jpg")

#sending response from DeepStack to RabbitMQ output queue
response = predictor.send_image(image_data, metadata)
output_queue = data_retrieve.write_data('Output', response)
data_retrieve.close()