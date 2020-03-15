import re
import copy
import json

from aliment_api.response.api_response import AlimentApiResponse

class RouterDispatcher():
    def __init__(self):
        self.allowedRoutes = dict()
        self.knownRoutes = dict()
        pass

    def addRoute(self, verb, path, callback):
        if (verb not in self.knownRoutes):
            self.knownRoutes[verb] = dict()
        
        self.knownRoutes[verb][path] = callback

    def dispatch(self, verb, path, body = None) -> AlimentApiResponse:
        for _verb in self.knownRoutes:
            if _verb == verb:
                for _path in self.knownRoutes[_verb]:
                    x = re.fullmatch(_path, path)
                    if None != x:
                        print ("ROUTE MATCH: ", _verb, _path)
                        return self.knownRoutes[_verb][_path](self.extractExtraArgs(x, body))
            
        return AlimentApiResponse(
            400, 
            {"status": "Bad request"}
        )

    def extractExtraArgs(self, matched_path, body):
        list = [i for i in matched_path.groups()]
        if body != None:
            list.append(json.loads(body.decode("utf-8")))
        return list