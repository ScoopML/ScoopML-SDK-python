import requests
class ScoopML():
     
    def __init__(self, url , text):
        session = requests.Session()
        self.session = session
        self.key = url
        self.text = text
        
    def get_predictions(self):
        response = requests.post(url, data={payload: text})
        info = response.json()
        return info
