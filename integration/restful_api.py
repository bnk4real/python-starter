# basic API caller
import http.client

# init HTTP Protocal
api = http.client.HTTPSConnection("randomuser.me")
api.request("GET", "/api/")

# get response 
response = api.getresponse()

# read response and decode to UTF-8
data = response.read().decode("UTF-8")
print(data)

# (Optional) at this point we can write a file
jsonFile = open("./data/user.json", "w")
jsonFile.write(data)
jsonFile.close()

api.close()