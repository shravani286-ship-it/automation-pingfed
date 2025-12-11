import requests
urlpost='https://localhost:9999/pf-admin-api/v1/keyPairs/signing/generate'

authpost = ('Administrator', '2Federate')
headerspost = {
	'accept': 'application/json',
    'x-xsrf-header': 'PingFederate',
}

bodypost = {
  "id": "12345",
  "commonName": "importtest_script",
  "subjectAlternativeNames": [],
  "organization": "trevonix",
  "city": "hyderabad",
  "state": "Telangana",
  "country": "IN",
  "validDays": 365,
  "keyAlgorithm": "RSA",
  "keySize": 2048,
  "signatureAlgorithm": "SHA256withRSA",
}

verifypost=False

response = requests.post(url=urlpost,headers=headerspost,json=bodypost,verify=verifypost,auth=authpost)
def post_request():   
 status = response.status_code
 print(status)
 return status
#print(status)
#assert status==201
#certdetails = response.json()
#print(certdetails['id'])