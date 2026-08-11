from googleapiclient.discovery import build
from dotenv import load_dotenv
import pandas as pd
import os
from pathlib import Path

# Load API Key
load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")

# Connect to YouTube API
youtube = build("youtube", "v3", developerKey=API_KEY)

# Uploads Playlist ID
playlist_id = "UUwFRGieumnh1MrM5F3D65Tg"

videos = []
next_page_token = None

while True:

    request = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id,
        maxResults=50,
        pageToken=next_page_token
    )

    response = request.execute()

    for item in response["items"]:

        video = {
            "Video ID": item["snippet"]["resourceId"]["videoId"],
            "Channel ID": "UCwFRGieumnh1MrM5F3D65Tg",
            "Title": item["snippet"]["title"],
            "Published Date": item["snippet"]["publishedAt"]
        }

        videos.append(video)

    next_page_token = response.get("nextPageToken")

    if next_page_token is None:
        break

df = pd.DataFrame(videos)

output_dir = Path("data/raw")
output_dir.mkdir(parents=True, exist_ok=True)

df.to_csv(output_dir / "videos.csv", index=False)

print(df.head())

print(f"\nTotal Videos Collected: {len(df)}")