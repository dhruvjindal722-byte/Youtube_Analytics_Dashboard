from dotenv import load_dotenv
import os
from googleapiclient.discovery import build

# load api key from .env file 
load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY
)

print("connected to Youtube Data API successfully!")
