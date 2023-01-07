import redis
import base64
from PIL import Image

  

class RedisReader():
    def __init__(self, host='localhost', port=6379, db=0, password='eYVX7EwVmmxKPCDmwMtyKVge8oLd2t81'):
        self.r = redis.Redis(host=host, port=port, db=db, password=password)
    
    def get_images(self, key):
        image_bytes = self.r.get(key)
        if image_bytes is None:
            return None
        image = base64.b64decode(image_bytes)
        return image

