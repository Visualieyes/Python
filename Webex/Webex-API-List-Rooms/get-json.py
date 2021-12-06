#Import the required dependancies, Request and urlopen libraries.
from urllib.request import Request, urlopen
import json


#Construct a request to the CMX URI.
req = Request('https://cmxlocationsandbox.cisco.com/api/config/v1/maps/info/DevNetCampus/DevNetBuilding/DevNetZone')

#Adds basic authentication to the request.
req.add_header('Authorization', 'Basic bGVhcm5pbmc6bGVhcm5pbmc=')

#Opens the request and gets a response from the CMX URI.
response = urlopen(req)

#Parses the response as a string and prints it to the console.
response_string = response.read().decode('utf-8')

#comment out line below
#print(response_string)

#json.loads() method loads the response_string into a JSON object.
json_object = json.loads(response_string)


#This line prints the elements dumps() method returns from the json_object
print(json.dumps(json_object, sort_keys=True, indent=4))



access_points = json_object['accessPoints']
for ap in access_points:
 print('Access Point: ' + ap['name'] + '\t mac: ' + ap['radioMacAddress'])


response.close()