from http.server import HTTPServer, BaseHTTPRequestHandler 
import json 

PORT = 8000
 
class APIHandler(BaseHTTPRequestHandler): 
    def do_GET(self): 
        if self.path == '/api/get-fruits': 
            self.send_response(200) 
            self.send_header('Content-Type', 'application/json') 
            self.end_headers() 
            fruits = ['apple', 'banana', 'mango', 'kiwi'] 
            self.wfile.write(json.dumps(fruits).encode()) 
        else: 
            self.send_response(404) 
 
httpProtocal = HTTPServer(('localhost', PORT), APIHandler) 
print("Listen and Serve at port", PORT)
httpProtocal.serve_forever()