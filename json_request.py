import requests

url = "https://jsonplaceholder.typicode.com/users/1"

response = requests.get(url)

if response.status_code == 200:
    user = response.json()
    print(f"Name: {user['name']}")
    print(f"Email: {user['email']}")
    print(f"Phone: {user['phone']}")
    print(f"Company: {user['company']['name']}")
else:
    print("Failed to fetch data.") 
