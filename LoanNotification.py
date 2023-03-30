# Import modules
import requests
import hashlib
from datetime import datetime

# URLs
demo_url = "https://remitademo.net/remita/exapp/api/v1/send/api/loansvc/data/api/v2/payday/post/loan"
live_url = "https://login.remita.net/remita/exapp/api/v1/send/api/loansvc/data/api/v2/payday/post/loan"

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


customerId = "456783897"
authorisationCode = "764386"
authorisationChannel = "USSD"
phoneNumber = "07038684773"
accountNumber = "1234657893"
currency = "NGN"
loanAmount = 2000
collectionAmount = 2100
dateOfDisbursement = "14-05-2021 10:16:18+0000"
dateOfCollection = "11-07-2021 10:16:18+0000"
totalCollectionAmount = "2100"
numberOfRepayments = 1
bankCode = "214"

Notification_Payload = {
  "customerId": f"{customerId}",
  "authorisationCode": f"{authorisationCode}",
  "authorisationChannel": f"{authorisationChannel}",
  "phoneNumber": f"{phoneNumber}",
  "accountNumber": f"{accountNumber}",
  "currency": f"{currency}",
  "loanAmount": f"{loanAmount}",
  "collectionAmount": f"{collectionAmount}",
  "dateOfDisbursement": f"{dateOfDisbursement}",
  "dateOfCollection": f"{dateOfCollection}",
  "totalCollectionAmount": f"{totalCollectionAmount}",
  "numberOfRepayments": f"{numberOfRepayments}",
  "bankCode": f"{bankCode}"
}
print(Notification_Payload)


# Post Function
def notification(url, headers, Notification_Payload):
	notify_Post = requests.post(url, headers= headers, json=Notification_Payload)
	return notify_Post.text

print(notification(demo_url, headers, Notification_Payload))
