from googleapiclient.discovery import build
from dotenv import load_dotenv
import pandas as pd
import os

# Load API Key
load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

# Connect to YouTube API
youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY
)

# Channel ID
channel_id = "UCwFRGieumnh1MrM5F3D65Tg"

# Request channel information
request = youtube.channels().list(
    part="snippet,statistics",
    id=channel_id
)

response = request.execute()

# Create an empty list
channel_data = []

# Extract information
for item in response["items"]:

    data = {
    "channel_id": item["id"],
    "channel_name": item["snippet"]["title"],
    "subscribers": int(item["statistics"]["subscriberCount"]),
    "total_views": int(item["statistics"]["viewCount"]),
    "total_videos": int(item["statistics"]["videoCount"]),
    "published_at": item["snippet"]["publishedAt"]
    }
    channel_data.append(data)

# Convert to DataFrame
df = pd.DataFrame(channel_data)
from pathlib import Path

output_dir = Path("data/raw")
output_dir.mkdir(parents=True, exist_ok=True)

# Save CSV
df.to_csv(output_dir / "channel.csv", index=False)

print("Channel data saved successfully!")