import requests
import json
import datetime

class ApiClient:

    # date = datetime.date + dateutil.relativedelta.relativedelta(months=-6)

    def __init__(self, api_key):
        self.base_url = 'https://eastus.api.cognitive.microsoft.com/text/analytics/v2.0/sentiment'
        self.api_key = api_key

    def get_sentiment(self, file_name):

        with open(file_name) as json_file:
            json_data = json.load(json_file)
        print({'documents':[{'text': 'Hello!'}, {'text': 'Boo'}]})

        headers = {'Ocp-Apim-Subscription-Key' : self.api_key, 'Accept' : 'application/json', 'Content-Type' : 'application/json'}

        data = requests.post(self.base_url, data=json.dumps([{'text': 'Hello!'}, {'text': 'Boo'}]), headers=headers)

        if(data.ok):
            return data
        else:
            print("Unsuccesful: " + str(data.status_code))
            return None