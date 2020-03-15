import json

class AlimentApiResponse:
    def __init__(self, code, payload):
        self.code = code
        self.payload = payload

    def getCode(self):
        return self.code
    
    def getPayload(self):
        return self.payload

    def getPayloadAsJSON(self):
        return json.dumps(self.payload)