# Import dependancies
import requests
import time

# Define payload content
payload = {
    'content': 'Your message here'

}

# Authorize account
header = {
    'authorization': 'Your auth code here'
}

# Send messages
for i in range (100000):
    time.sleep(Your delay here in seconds)
    r = requests.post('Your channel request url here', data=payload, headers=header)
    print("Sent message successfully!")
