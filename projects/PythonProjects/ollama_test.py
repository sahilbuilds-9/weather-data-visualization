import requests

url = "http://localhost:11434/api/generate"

data = {
    "model": "qwen3:8b",
    "prompt": "Explain Python OOP in simple terms",
    "stream": False
}

response = requests.post(url, json=data)

print(response.json()["response"])