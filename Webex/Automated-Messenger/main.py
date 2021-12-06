import requests
import json

apiUrl = "https://api.ciscospark.com/v1/messages"
access_token = "YOUR_API_KEY"
httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}



emails = json.loads(open('emails.json').read())

message = "YOUR MESSAGE"



for email in emails:
  body = {"toPersonEmail" : email, "text" : message}
  response = requests.post(url=apiUrl, json=body, headers=httpHeaders)

  print(response.status_code)
  print(response.text)

  print ('Sending:', email) 