import requests
from datetime import datetime, timezone

USERNAME = "vinuaish"

# Current year and month (UTC)
now = datetime.now(timezone.utc)
year = now.year
month = f"{now.month:02d}"

# Chess.com API URL
archive_url = f"https://api.chess.com/pub/player/{USERNAME}/games/{year}/{month}"

try:
    response = requests.get(archive_url, timeout=10)
    response.raise_for_status()

    data = response.json()
    games = data.get("games", [])

    if not games:
        print(f"No games found for {USERNAME} in {year}-{month}.")
    else:
        print(f"Found {len(games)} game(s) for {USERNAME} in {year}-{month}.\n")

        # Get the latest game
        latest_game = games[-1]

        white = latest_game["white"]["username"]
        black = latest_game["black"]["username"]
        white_result = latest_game["white"]["result"]
        black_result = latest_game["black"]["result"]
        end_time = datetime.fromtimestamp(
            latest_game["end_time"], tz=timezone.utc
        )

        print("Latest Game")
        print("-" * 40)
        print(f"Players : {white} vs {black}")
        print(f"Result  : White = {white_result}, Black = {black_result}")
        print(f"Ended   : {end_time.strftime('%Y-%m-%d %H:%M UTC')}")
        print(f"Game URL: {latest_game.get('url', 'N/A')}")

        print("\nPGN:")
        print("-" * 40)
        print(latest_game["pgn"])

except requests.exceptions.RequestException as e:
    print("Connection error:", e)
