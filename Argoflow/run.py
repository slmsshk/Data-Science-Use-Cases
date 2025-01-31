import requests

# payload = {"prompt": "falling"}
payload = {"prompt": input('Enter your prompt: \n')}

headers = {"Content-Type": "application/json"}

url = "http://localhost:8000/generate"


response = requests.post(url,json=payload,headers=headers)


print(response.json()['generated_text'],response)


# import requests

# Define the URL of the Flask application
# url = "http://localhost:8080/"

# Send a GET request to the Flask application
# response = requests.get(url)

# Print the response text (this should be "Hello, World!")
# print(response.text)
