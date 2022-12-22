import requests

class DeepStackClient:
    def __init__(self):
        self.api_url = "https://localhost:80/v1/vision/object_detection"

    def send_image(self, image_path, message):
        #read the image file and set the content type
        headers = {"Content-Type": "image/jpeg"}

        #metadata in the request body
        data = {"message": message}

        #send image to DeepStack
        response = requests.post(
            self.api_url, headers=headers, data=open(image_path, "rb"), 
             json=data
        )

        return response


predictor = DeepStackClient()
response = predictor.send_image("C:\\Users\\MT\\Desktop\\Adaptor DeepStack\\App\\Redis_load_images\\kitty.jpg", "date")
print(response)