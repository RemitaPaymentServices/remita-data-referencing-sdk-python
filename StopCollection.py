# Import modules
import requests
import hashlib
from datetime import datetime

# URLs
demo_url = "https://remitademo.net/remita/exapp/api/v1/send/api/loansvc/data/api/v2/payday/stop/loan"
live_url = "https://login.remita.net/remita/exapp/api/v1/send/api/loansvc/data/api/v2/payday/stop/loan"


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
authorization = "remitaConsumerKey=" + apiKey + ", remitaConsumerToken=" +apiHash

# The Payload to Post to the URL
headers = {
	"Api_Key": f"{apiKey}",
    "Merchant_id": f"{merchantId}",
	"Request_id": f"{requestId}",
	"Authorization": f"{authorization}"
}

authorisationCode = "764386"
customerId = "456783897"
mandateReference = "280008217475"

Stop_Payload = {
	"authorisationCode": f"{authorisationCode}",
	"customerId": f"{customerId}",
	"mandateReference": f"{mandateReference}"
}


# Post Function
def stopcollection(url, headers, Stop_Payload):
	stopcollection_Post = requests.post(url, headers= headers, json=Stop_Payload)
	return stopcollection_Post.text


print(stopcollection(demo_url, headers, Stop_Payload))
