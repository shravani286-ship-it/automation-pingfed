from src.main import post_request
#assert post_request(201)
status = post_request()

print("Status code:", status)

if status == 201:
    print("API call successful!")
else:
    print("API call failed!")