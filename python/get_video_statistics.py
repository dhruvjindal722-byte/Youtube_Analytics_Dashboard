from googleapiclient.discovery import build
from dotenv import load_dotenv
import pandas as pd
import os

# Load API Key
load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = build("youtube", "v3", developerKey=API_KEY)

# Read videos.csv
videos_df = pd.read_csv("data/raw/videos.csv")

print(videos_df.head())
print(f"Total Videos: {len(videos_df)}")

# Get all Video IDs
video_ids = videos_df["Video ID"].tolist()
statistics_data = []
# Process videos in batches of 50
for i in range(0, len(video_ids), 50):

    batch = video_ids[i:i+50]

    request = youtube.videos().list(
        part="statistics,contentDetails",
        id=",".join(batch)
    )

    response = request.execute()

    print(f"Batch {(i//50)+1}")

    
    for item in response["items"]:

        statistics_data.append({
            "Video ID": item["id"],
            "Views": item["statistics"].get("viewCount", 0),
            "Likes": item["statistics"].get("likeCount", 0),
            "Comments": item["statistics"].get("commentCount", 0),
            "Duration": item["contentDetails"]["duration"]
        })
import pathlib

stats_df = pd.DataFrame(statistics_data)

output_dir = pathlib.Path("data/raw")
output_dir.mkdir(parents=True, exist_ok=True)

stats_df.to_csv(output_dir / "video_statistics.csv", index=False)

print("Video statistics saved successfully!")
print(stats_df.head())