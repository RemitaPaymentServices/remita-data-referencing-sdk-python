# Import modules
import requests
import hashlib
from datetime import datetime
import random
import math

# URLs
demo_url = "https://remitademo.net/remita/exapp/api/v1/send/api/loansvc/data/api/v2/payday/salary/history/ph"
live_url = "https://login.remita.net/remita/exapp/api/v1/send/api/loansvc/data/api/v2/payday/salary/history/ph"


# Hash Function
def hash512(credentials):
    hashed_input = hashlib.sha512(credentials.encode('utf-8'))
    hex_dig = hashed_input.hexdigest()
    return hex_dig


# Credentials
apiKey = "Q1dHREVNTzEyMzR8Q1dHREVNTw=="
merchantId = "27768931"
requestId = str(datetime.now())
apiToken = "SGlQekNzMEdMbjhlRUZsUzJCWk5saDB6SU14Zk15djR4WmkxaUpDTll6bGIxRCs4UkVvaGhnPT0="

# Get the Hash Value of credentials
apiHash = hash512(apiKey + requestId + apiToken)

authorization = "remitaConsumerKey=" + apiKey + ", remitaConsumerToken=" + apiHash

# Get a Random value
randomnumber = math.floor(random.random() * 1101233)

# Define Variables
phonenumber = "07038684773"
authorisationCode = randomnumber

# The Payload to Post to the URL
headers = {
	"Api_Key": f"{apiKey}",
    "Merchant_id": f"{merchantId}",
	"Request_id": f"{requestId}",
	"Authorization": f"{authorization}"
}

history_Payload = {
   "authorisationCode": f"{authorisationCode}",
   "phoneNumber": f"{phonenumber}",
   "authorisationChannel": "USSD"
}


# Post Function
def checkhistory(url, headers, history_Payload):
	history_Post = requests.post(url, headers= headers, json=history_Payload)
	return history_Post.text

print(checkhistory(demo_url, headers, history_Payload))
