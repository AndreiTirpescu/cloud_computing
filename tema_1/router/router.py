import re
import copy

class RouterDispatcher():
    def __init__(self):
        self.allowedRoutes = dict()
        pass

    def addRoute(self, verb, path, callback):
        self.allowedRoutes[(verb, path)] = callback
   
    def dispatch(self, verb, path, body = None):
        pathCpy = copy.deepcopy(path)
        pathArgList = pathCpy.split("/")
        if (len(pathArgList) > 2):
            pathArgList = pathArgList[2:]
        
        for _verb, _path in self.allowedRoutes.keys():
            if _verb == verb and path[0:len(_path)] == _path:
                return self.allowedRoutes[(verb, path)]()

        return "404"