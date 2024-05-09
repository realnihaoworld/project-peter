import requests

response = requests.post("http://127.0.0.1:5000/", data={"url": "test.com"})
print(response.text)

r = requests.get('http://127.0.0.1:5000/get')
print(f"get request: {r.text}")