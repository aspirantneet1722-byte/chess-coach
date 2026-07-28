import requests
from datetime import datetime, timezone

# ==========================
# CHANGE ONLY THIS
# ==========================
USERNAME = "vinuaish"

# Chess.com recommends including a User-Agent
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

# Current year and month
now = datetime.now(timezone.utc)
year = now.year
month = f"{now.month:02d}"

# Chess.com API URL
archive_url = f"https://api.chess.com/pub/player/{USERNAME}/games/{year}/{month}"

print("Connecting to Chess.com...")
print("URL:", archive_url)

try:
    response = requests.get(archive_url, headers=HEADERS, timeout=20)

    print("Status Code:", response.status_code)

    if response.status_code == 200:
        data = response.json()
        games = data.get("games", [])

        if len(games) == 0:
            print("\nNo games found this month.")
        else:
            print(f"\nFound {len(games)} game(s).\n")

            for i, game in enumerate(games, start=1):
                white = game["white"]["username"]
                black = game["black"]["username"]

                white_result = game["white"]["result"]
                black_result = game["black"]["result"]

                end_time = datetime.fromtimestamp(
                    game["end_time"],
                    tz=timezone.utc
                )

                print("=" * 60)
                print(f"Game {i}")
                print(f"{white} vs {black}")
                print(f"White Result : {white_result}")
                print(f"Black Result : {black_result}")
                print("Finished     :", end_time.strftime("%Y-%m-%d %H:%M UTC"))

                # PGN text
                pgn = game["pgn"]

                # Save PGN to a file
                filename = f"game_{i}.pgn"

                with open(filename, "w", encoding="utf-8") as f:
                    f.write(pgn)

                print(f"Saved PGN as {filename}")

    elif response.status_code == 404:
        print("\nUsername not found.")
        print("Check if the username is correct.")

    elif response.status_code == 403:
        print("\n403 Forbidden")
        print("Chess.com rejected the request.")
        print("This usually happens because of the platform you are running on or a blocked request.")

    else:
        print("\nRequest failed.")
        print("Response:")
        print(response.text)

except Exception as e:
    print("\nError:")
    print(e)
