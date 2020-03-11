import os
from http.server import HTTPServer 
from http.server import BaseHTTPRequestHandler
from router.router import RouterDispatcher
from myip.myip import MyIpService
from ipinfo.ipinfo import IpInfoService
from weather.weatherinfo import WeatherInfoService

HOST = "127.0.0.1"
PORT = 8000

class CustomServerHandler(BaseHTTPRequestHandler):
    def __init__(self, router, *args):
        self.routerDispatcher = router
        BaseHTTPRequestHandler.__init__(self, *args)
    
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write(bytes(self.routerDispatcher.dispatch("GET", self.path) , 'utf-8'))


class Server:
    def __init__(self, HOST, PORT):
        self.host = HOST
        self.port = PORT
        self.myIpApiService = MyIpService()
        self.ipInfoService = IpInfoService()
        self.weatherInfoService = WeatherInfoService()
    
    def run(self):
        dispatcher = RouterDispatcher()
        
        dispatcher.addRoute("GET", "/ipinfo", self.ipInfoService.execute)
        dispatcher.addRoute("GET", "/myip", self.myIpApiService.execute)
        dispatcher.addRoute("GET", "/weather", self.weatherInfoService.execute)
        
        def handler(*args):
            CustomServerHandler(dispatcher, *args)
        
        httpd = HTTPServer((HOST, PORT), handler)
        httpd.serve_forever()


if __name__ == '__main__':
    webServer = Server(HOST, PORT)
    webServer.run()