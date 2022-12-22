import base64
import redis
import os


#connect to the Redis server
r = redis.Redis(host='localhost', port=6379, db=0, password='eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81')

image_dir='C:\\Users\\MT\\Desktop\\Adaptor DeepStack\\App\\Redis_load_images'
image_files=[f for f in os.listdir(image_dir) if f.endswith(('.jpg', '.png', '.jfif'))]

#open and encode the image as a base64 string for Redis
for image_file in image_files:
    with open(os.path.join(image_dir, image_file), 'rb') as f:
        image_data = base64.b64encode(f.read())
    
    #store the image in Redis
    r.set(f'{image_file}', image_data)

#print(r.ping()) #verification
