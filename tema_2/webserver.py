import os
from http.server import HTTPServer 
from http.server import BaseHTTPRequestHandler
from router.router import RouterDispatcher
from aliment_api.controller.aliment_api_controller import AlimentApiController
from aliment_api.response.api_response import AlimentApiResponse

HOST = "127.0.0.1"
PORT = 8000

class CustomServerHandler(BaseHTTPRequestHandler):
    def __init__(self, router, *args):
        self.routerDispatcher = router
        BaseHTTPRequestHandler.__init__(self, *args)
    
    def do_GET(self):
        api_response = self.routerDispatcher.dispatch("GET", self.path)
        self.setJSONHeaders(api_response.getCode())
        self.wfile.write(bytes(api_response.getPayloadAsJSON(), 'utf-8'))

    def do_POST(self):
        
        api_response = self.routerDispatcher.dispatch("POST", self.path, body=self.extractBody())
        self.setJSONHeaders(api_response.getCode())
        self.wfile.write(bytes(api_response.getPayloadAsJSON(), 'utf-8'))
    
    def do_PUT(self):
        api_response = self.routerDispatcher.dispatch("PUT",  self.path, body=self.extractBody())
        self.setJSONHeaders(api_response.getCode())
        self.wfile.write(bytes(api_response.getPayloadAsJSON(), 'utf-8'))

    def do_DELETE(self):
        api_response = self.routerDispatcher.dispatch("DELETE",  self.path)
        self.setJSONHeaders(api_response.getCode())
        self.wfile.write(bytes(api_response.getPayloadAsJSON(), 'utf-8'))
    
    def setJSONHeaders(self, resp_code):
        self.send_response(resp_code)
        self.send_header('Content-type','text/json')
        self.end_headers()

    def extractBody(self):
        return self.rfile.read(
            int(self.headers.get('Content-Length'))
        )

class Server:
    def __init__(self, HOST, PORT):
        self.host = HOST
        self.port = PORT
        self.aliment_api_controller = AlimentApiController()
    
    def run(self):
        dispatcher = RouterDispatcher()

        dispatcher.addRoute("GET", "\/aliment\/([a-zA-Z0-9]+)", self.aliment_api_controller.get_aliment)
        dispatcher.addRoute("GET", "/aliments", self.aliment_api_controller.get_aliments)
        
        dispatcher.addRoute("POST", "/aliment", self.aliment_api_controller.post_aliment)
        dispatcher.addRoute("POST", "/aliments", self.aliment_api_controller.post_aliments)

        dispatcher.addRoute("PUT", "/aliment", self.aliment_api_controller.put_aliment)
        dispatcher.addRoute("PUT", "/aliments", self.aliment_api_controller.put_aliments)

        dispatcher.addRoute("DELETE", "/aliment/([a-zA-Z0-9]+)", self.aliment_api_controller.delete_aliment)
        dispatcher.addRoute("DELETE", "/aliments", self.aliment_api_controller.delete_aliments)
        
        def handler(*args):
            CustomServerHandler(dispatcher, *args)
        
        httpd = HTTPServer((HOST, PORT), handler)
        httpd.serve_forever()


if __name__ == '__main__':
    webServer = Server(HOST, PORT)
    webServer.run()