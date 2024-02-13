# Basic web server 2

import http.server
import socketserver
import json

PORT = 8090

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        # create object json
        message = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        # convert python to JSON 
        jsonMsg = json.dumps(message)
        self.wfile.write(jsonMsg.encode())

with socketserver.TCPServer(("", PORT), CustomHandler) as httpd:
    print("Serving at port", PORT)
    httpd.serve_forever()