import requests

url = "https://api.chess.com/pub/player/vinuaish"

headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

response = requests.get(url, headers=headers)

print("Status:", response.status_code)
print(response.text)
