# Basic web server API with data from database
import http.server
import socketserver
import json
import sqlite3
import logging

PORT = 8090 # Ports
conn = sqlite3.connect("sqlite_test1.db") # Connect to database
cursor = conn.cursor() # cursor

# Create User Class
class User:
    def __init__(
            user, 
            id : int, 
            username : str, 
            email : str,
        ):
        user.Id = int(id)
        user.Username = str(username)
        user.Email = str(email)

class CustomHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(set):
        if set.path == '/api/users': 
            set.send_response(200)
            set.send_header('Content-type', 'application/json')
            set.end_headers()

            # Query Statement
            query = "SELECT id, username, email FROM users;"
            cursor.execute(query)
            rows = cursor.fetchall()

            # Declare empty list await to append data into
            users = []

            # Create User objects and append them to the list
            for row in rows:
                user = User(row[0], row[1], row[2])
                users.append(user.__dict__)

            # Convert list of dictionaries to JSON
            jsonMsg = json.dumps(users)
            set.wfile.write(jsonMsg.encode())
            logging.basicConfig(filename='logging.log', encoding='utf-8', level=logging.DEBUG)
            logging.debug(jsonMsg)
        else:
            set.send_response(404)
            set.send_header('Content-type', 'application/json')
            set.end_headers()
            message = {
                "status": 404,
                "message": "resources not found",
            }
            jsonMsg = json.dumps(message)
            set.wfile.write(jsonMsg.encode())
            logging.basicConfig(filename='logging.log', encoding='utf-8', level=logging.DEBUG)
            logging.debug(jsonMsg)

with socketserver.TCPServer(("localhost", PORT), CustomHandler) as httpd:
    print("Listen and Serve at port", PORT)
    httpd.serve_forever()