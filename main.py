import requests

USERNAME = "vinuaish"

url = f"https://api.chess.com/pub/player/{USERNAME}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Connected to Chess.com!")
    print("Username:", data["username"])
    print("Name:", data.get("name", "Not available"))
else:
    print("Connection failed:", response.status_code)
