import os
import urllib.request
import json

class IpInfoService():
    def __init__(self):
        super().__init__()
        self.payload = []
    
    def loadPayLoad(self, payLoad):
        self.payload = payLoad

    def execute(self, args = None):
        
        resp1 = urllib.request.urlopen("https://api.ipify.org/").read()
        resp2 = urllib.request.urlopen("http://ip-api.com/json/" + resp1.decode('utf-8')).read()

        apiRespPath = os.path.join(os.path.dirname(__file__), 'public/ipinfo.html')
        
        apiRespContent = open(apiRespPath, "r").read()
        
        respObj = json.loads(resp2.decode('utf-8'))

        apiRespContent = apiRespContent.replace("{py_template: COUNTRY}", respObj['country'])
        apiRespContent = apiRespContent.replace("{py_template: CITY}", respObj['city'])
        apiRespContent = apiRespContent.replace("{py_template: LAT}", str(respObj['lat']))
        apiRespContent = apiRespContent.replace("{py_template: LON}", str(respObj['lon']))

        return apiRespContent

    