import requests
import random
import os
import string
import json
import time


#Use a proxies in a dictionary to hide the ip of the request
proxies_dict = {										
	'http' : 'socks5://152.1.204.8:1080',
	'https' : 'socks5://152.1.204.8:1080'
}

email_domain = ["@hotmail.com", "@gmail.com", "@outlook.com", "@yahoo.com"]   #added for more variation amongst emails

url = 'http://www.universalstudiospromos.com/happybirthday/regNow.php'

random.seed = (os.urandom(1024)) 

names = json.loads(open('names.json').read())



for name in names:
	time.sleep(3)    #Exception may be raised if too many requests are sent
	num = ''.join(random.choice(string.digits)) + str(random.randrange(0,999)) 
	name_extra = ''.join(random.choice(names))	   	
	email = name.lower() + name_extra + num + email_domain[random.randrange(0,4)]  #revised to descrease liklihood of collision of real email
	r = requests.post(url, allow_redirects=False, proxies=proxies_dict, data={
		'name' : name, 
		'email' : email
	})
	
# 	print(r.request.headers,'\n')  #uncomment to see headders sent to the server
# 	print(r.headers,'\n')   	   #uncomment to see headers sent back by the server
	
	print ('Sending name:', name, 'email:', email) 