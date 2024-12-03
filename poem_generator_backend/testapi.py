import requests

# Define the endpoint and prompt
url = "http://127.0.0.1:5000/generate"
data = {"prompt": "The moonlight shone brightly"}

# Send POST request
response = requests.post(url, json=data)

# Print the response
print(response.json())
