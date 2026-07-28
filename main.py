import requests

USERNAME = "vinuaish"

url = f"https://api.chess.com/pub/player/{USERNAME}/games"

response = requests.get(url)

if response.status_code == 200:
    print("Connected to Chess.com successfully!")
else:
    print("Unable to connect. Status:", response.status_code)
