import requests
import json
import string

from httpsig.requests_auth import HTTPSignatureAuth
KEY_ID = '53a90c7f-6bc5-4c36-ac3d-03b8a90571c4'
SECRET = 'ca6df62d-9c56-4afc-9909-9da93a4a8a24'

signature_headers = ['(request-target)', 'accept', 'date']
headers = {
    'Accept': 'application/json',
    'Date': "Mon, 17 Feb 2014 06:11:05 GMT"
}

auth = HTTPSignatureAuth(key_id=KEY_ID, secret=SECRET, algorithm='hmac-sha256', headers=signature_headers)

req = requests.get('http://jms.l510881.com/api/v1/assets/assets/', auth=auth, headers=headers)
json1 = req.content.decode('utf-8')
data = json.loads(json1)

for i in data:
    if "dac90d88-4355-4ec1-bab6-4ce5f815677e" in i['labels']:
        ip = i['ip']
        port = i['protocols'][0].split("/")[1]
        print(ip, port)
