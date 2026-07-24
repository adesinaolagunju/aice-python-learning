import requests

url = "https://api.github.com"

response = requests.get(url)

print(f"Status.code: {response.status_code}")
print(f"Response type: {type(response)}")

if response.status_code == 200:
    print("Connection successful!")
else:
    print("Connection failed.") 
