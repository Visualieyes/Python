import requests


#define a couple of global variables. These variables will hold the URL of the /rooms API, and your developer access token
apiUrl = "https://api.ciscospark.com/v1/rooms"
access_token = "NGRiODBkZjktMmFkOS00MjA2LThiNGUtOGQ4ODljMTcwZmM3OGM0MWNiOGQtNmY0_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"  #update token after 12 hours


# create a Python "dictionary" type variable which will hold the HTTP headers:
httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}


#We can define query parameters as well to filter the results. This variable will have a dictionary data-type as well. 
#For our GET request we would like to receive room details sorted by last activity, and with no more than 2 results returned:

# Note: Query parameters in a GET method act as a filters to the query and are optional.

queryParams = {"sortBy" : "lastactivity", "max" : "2"}



#Perform the API request.
#Here we provide the necessary arguments for the get() method, which we stored in the variables above, with the output of the request stored in a response variable:
response = requests.get(url=apiUrl, headers=httpHeaders, params=queryParams)




#Output the returned status code and possible text to the console:
print(response.status_code)
print(response.text)