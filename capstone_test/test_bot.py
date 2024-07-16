#!/usr/bin/env python3
import requests

url = "http://127.0.0.1:5000/ask"
payload = {"query": "How is the weather today?"}
headers = {"Content-Type": "application/json"}

response = requests.post(url, json=payload, headers=headers)
print(response.json())
