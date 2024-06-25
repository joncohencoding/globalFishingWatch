import requests
import json

URL = "https://jsonplaceholder.typicode.com/users"

print("Search by UserName")
user = input("> ")
queryURL = URL + f"?username={user}"
response = requests.get(queryURL)

userData = json.loads(response.text)[0]

name = userData["name"]
email = userData["email"]
phone = userData["phone"]

print(f"{name} can be reached via the following methods")
print(f"Email: {email}")
print(f"Phone: {phone}")