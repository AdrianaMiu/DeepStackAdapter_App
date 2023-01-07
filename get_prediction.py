import requests
import json



class DeepStackClient:
    def __init__(self):
        self.api_url = "http://localhost:80/v1/vision/detection"

    def send_image(self, image_data, json_data=None):
        
        try:
            response = requests.post(self.api_url, files={"image":image_data, "json":json_data})
            output = {"OUTPUT":{"PREDICTIONS":[]}}
            if response.status_code != 200:
                raise Exception(f'Error: {response.text}')
            else:
                json_data = json.loads(json_data.decode('utf-8'))
                for object in response.json()["predictions"]:
                    boundingbox = [[object["x_min"], object["y_min"]], 
                                   [object["x_max"], object["y_max"]]]
                    confidence = object['confidence']
                    label = object['label']
                    dict = {"boundingbox":boundingbox, "confidence":confidence, "label":label }
                    output["OUTPUT"]['PREDICTIONS'].append(dict)
                    output["OUTPUT"].update({'success':response.json()['success']})
                json_data.update(output)
                return json_data
        except Exception as e:
            #return the error msg if there was an issue with the request
            return {'ERROR':str(e)}
