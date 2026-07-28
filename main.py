import requests
from datetime import datetime, timezone

USERNAME = "vinuaish"

HEADERS = {
    "User-Agent": "ChessCoachApp/1.0 (contact: your-email@example.com)"
}

now = datetime.now(timezone.utc)
year = now.year
month = f"{now.month:02d}"

archive_url = f"https://api.chess.com/pub/player/{USERNAME}/games/{year}/{month}"

response = requests.get(archive_url, headers=HEADERS)

if response.status_code == 200:
    data = response.json()
    games = data.get("games", [])

    if not games:
        print(f"No games found for {USERNAME} in {year}-{month}.")
    else:
        print(f"Found {len(games)} game(s) for {USERNAME} in {year}-{month}:\n")

        for game in games:
            white = game["white"]["username"]
            black = game["black"]["username"]
            white_result = game["white"]["result"]
            black_result = game["black"]["result"]
            end_time = datetime.fromtimestamp(game["end_time"], tz=timezone.utc)
            pgn_url = game.get("url", "N/A")

            print(f"- {white} vs {black}")
            print(f"  Result: white={white_result}, black={black_result}")
            print(f"  Ended: {end_time.strftime('%Y-%m-%d %H:%M UTC')}")
            print(f"  Link: {pgn_url}\n")
else:
    print("Connection failed:", response.status_code)
