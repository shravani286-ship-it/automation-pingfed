import requests

def post_request():
    url = 'https://Trevonix-Device:9999/pf-admin-api/v1/keyPairs/signing/generate'
    auth = ('Administrator', '2Federate')
    headers = {
        'accept': 'application/json',
        'x-xsrf-header': 'PingFederate',
    }
    body = {
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
    verify_ssl = False

    response = requests.post(
        url=url,
        headers=headers,
        json=body,
        verify=verify_ssl,
        auth=auth
    )

    print(response.status_code)
    return response.status_code

#print(status)
#assert status==201
#certdetails = response.json()
#print(certdetails['id'])