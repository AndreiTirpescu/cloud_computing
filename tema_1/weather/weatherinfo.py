import os
import urllib.request
import json

class WeatherInfoService():
    def __init__(self):
        super().__init__()
        self.apiKey = ""

    def loadApiKey(self):
        keyPath =  os.path.join(os.path.dirname(__file__), 'config/apikey.txt')
        self.apiKey = open(keyPath, "r").read()

    def execute(self, args = None):
        self.loadApiKey()
        
        resp1 = urllib.request.urlopen("https://api.ipify.org/").read()
        resp2 = urllib.request.urlopen("http://ip-api.com/json/" + resp1.decode('utf-8')).read()
        
        respObj = json.loads(resp2.decode('utf-8'))

        resp3 = urllib.request.urlopen("https://api.darksky.net/forecast/" + self.apiKey + "/" + str(respObj['lat']) + "," + str(respObj['lon'])).read()

        apiRespPath = os.path.join(os.path.dirname(__file__), 'public/weatherinfo.html')
        
        apiRespContent = open(apiRespPath, "r").read()
        respObj2 = json.loads(resp3.decode('utf-8'))
        apiRespContent = apiRespContent.replace("{py_template: SUMARY}", respObj2['currently']['summary'])

        return apiRespContent
    