import conf
import requests
import os
# Get token
payload = {
    "grant_type": "client_credentials",
    "client_id": os.environ["CLIENT_ID"],
    "client_secret": os.environ["CLIENT_SECRET"],
    "audience": os.environ["AUDIENCE"]
}
headers = {'content-type': "application/json"}

res = requests.post(os.environ["DOMAIN"] + "/oauth/token", payload, headers)
res.raise_for_status()
access_token = res.json()['access_token']
print "ACCESS TOKEN: \n{}".format(access_token)
