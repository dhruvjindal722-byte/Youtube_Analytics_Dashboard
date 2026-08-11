import pandas as pd
from sqlalchemy import create_engine

# PostgreSQL connection details
USERNAME = "postgres"
PASSWORD = "dhruv"
HOST = "localhost"
PORT = "5432"
DATABASE = "youtube_analytics"

# Create connection
engine = create_engine(
    f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"
)

print("Connected to PostgreSQL successfully!")


import pandas as pd

# Load channel.csv
#channel_df = pd.read_csv("data/raw/channel.csv")

# Insert into PostgreSQL
#channel_df.to_sql(
 #   "channels",
  #  engine,
   # if_exists="append",
   # index=False
#)

#print("Channels table loaded successfully!")

# -----------------------------
# Load CSV files
# -----------------------------
videos_df = pd.read_csv("data/raw/videos.csv")
stats_df = pd.read_csv("data/raw/video_statistics.csv")
# Rename videos.csv columns
videos_df.columns = [
    "video_id",
    "channel_id",
    "title",
    "published_at"
]

# Rename video_statistics.csv columns
stats_df.columns = [
    "video_id",
    "views",
    "likes",
    "comments",
    "duration"
]
# Merge videos and statistics on video_id
merged_df = pd.merge(
    videos_df,
    stats_df,
    on="video_id",
    how="inner"
)

print("Videos CSV rows:", len(videos_df))
print("Statistics CSV rows:", len(stats_df))
print("Merged rows:", len(merged_df))
 
merged_df.to_sql(
    "videos",
    engine,
    if_exists="append",
    index=False
)

print("Videos table loaded successfully!")