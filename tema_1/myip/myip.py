import os
import urllib.request

class MyIpService():
    def __init__(self):
        super().__init__()

    def execute(self, args = None):
        resp = urllib.request.urlopen("https://api.ipify.org/").read()

        apiRespPath = os.path.join(os.path.dirname(__file__), 'public/myip.html')
        
        apiRespContent = open(apiRespPath, "r").read()
        
        apiRespContent = apiRespContent.replace("{py_template: IP}", resp.decode('utf-8'))

        return apiRespContent
    