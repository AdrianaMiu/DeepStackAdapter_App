import redis
import base64
from PIL import Image

  

class RedisReader():
    def __init__(self, host='localhost', port=6379, db=0, password='eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81'):
        self.r = redis.Redis(host=host, port=port, db=db, password=password)
    
    def get_images(self):
        #get a list of all keys
        keys = self.r.keys()

        for key in keys:
            if key.endswith((b'.jpg', b'.png')):
                return self.r.get(key)

reader = RedisReader()
reader.get_images()