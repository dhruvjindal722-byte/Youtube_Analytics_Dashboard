# YouTube Channel Analytics Dashboard

An end-to-end Business Intelligence project using the YouTube Data API v3, Python, PostgreSQL, SQL, DAX, Power BI, and VS Code.

## Project Overview

YouTube channel and video data is collected through the YouTube Data API v3, processed with Python, stored in PostgreSQL, analyzed using SQL, and presented through an interactive Power BI dashboard.

**Workflow:**

YouTube Data API v3 → Python → PostgreSQL → SQL Analysis → Power BI

## Channel

- Channel: Regaltos
- Handle: @soulregaltos9810
- Channel creation date shown in the dashboard: 11 Dec 2015

## Dashboard KPIs

Values visible in the supplied dashboard:

- Total Videos: 1,729
- Total Views: 652M
- Total Likes: 58M
- Total Comments: 700K
- Avg Views per Video: 377.06K
- Subscribers: 2.48M
- Data Last Refreshed: 8 Aug 2026

## Technology Stack

| Technology | Purpose |
|---|---|
| YouTube Data API v3 | Real YouTube data acquisition |
| Python | API extraction and data processing |
| VS Code | Development environment |
| PostgreSQL | Data storage |
| SQL | Business analysis |
| Power BI | Interactive dashboard |
| DAX | Dynamic measures |
| GitHub | Portfolio and version control |

## Data Architecture

```text
YouTube Data API v3
        ↓
Python Extraction
        ↓
PostgreSQL
        ↓
SQL Analysis
        ↓
Power BI Data Model
        ↓
Interactive Dashboard
```

## Database Tables

### `public_channels`

Channel-level information such as channel ID, channel name, subscribers, and metadata.

### `public_videos`

Video-level information such as video ID, title, publication date/time, views, likes, and comments.

## API Key Security

The YouTube API key must never be committed to GitHub.

Use a `.env` file:

```env
YOUTUBE_API_KEY=your_private_api_key_here
```

Load it in Python:

```python
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")
```

Install dependencies:

```bash
pip install google-api-python-client python-dotenv
```

Use `.gitignore`:

```gitignore
.env
*.key
*.pem
__pycache__/
.venv/
```

Commit only a safe `.env.example`:

```env
YOUTUBE_API_KEY=your_api_key_here
```

## SQL Analysis

### Total Videos

```sql
SELECT COUNT(DISTINCT video_id) AS total_videos
FROM public_videos;
```

### Total Views, Likes and Comments

```sql
SELECT
    SUM(views) AS total_views,
    SUM(likes) AS total_likes,
    SUM(comments) AS total_comments
FROM public_videos;
```

### Average Views per Video

```sql
SELECT AVG(views) AS avg_views_per_video
FROM public_videos;
```

### Top 10 Videos by Views

```sql
SELECT title, views, likes, comments
FROM public_videos
ORDER BY views DESC
LIMIT 10;
```

### Views by Year

```sql
SELECT
    EXTRACT(YEAR FROM published_at) AS published_year,
    COUNT(DISTINCT video_id) AS total_videos,
    SUM(views) AS total_views
FROM public_videos
GROUP BY EXTRACT(YEAR FROM published_at)
ORDER BY published_year;
```

### Views by Month

```sql
SELECT
    EXTRACT(MONTH FROM published_at) AS published_month,
    COUNT(DISTINCT video_id) AS total_videos,
    SUM(views) AS total_views
FROM public_videos
GROUP BY EXTRACT(MONTH FROM published_at)
ORDER BY published_month;
```

### Engagement Analysis

```sql
SELECT
    title,
    views,
    likes,
    comments,
    CASE
        WHEN views > 0
        THEN ROUND((likes::numeric / views) * 100, 2)
        ELSE 0
    END AS like_rate_percentage
FROM public_videos
ORDER BY views DESC
LIMIT 10;
```

## Power BI DAX Measures

```DAX
Total Videos =
DISTINCTCOUNT('public videos'[video_id])

Total Views =
SUM('public videos'[views])

Total Likes =
SUM('public videos'[likes])

Total Comments =
SUM('public videos'[comments])

Avg Views per Video =
DIVIDE([Total Views], [Total Videos])
```

## Dashboard Features

### KPI Cards

- Total Videos
- Total Views
- Total Likes
- Total Comments
- Avg Views per Video

### Interactive Filters

- Published Year
- Published Month
- Video Title

### Main Visuals

- Top 10 Videos by Views
- Views by Year
- Top 10 Videos by Likes
- Likes vs Comments
- Monthly Views Trend
- Top 10 Videos by Comments
- Average engagement metrics
- Channel information panel

## Business Questions

The dashboard helps answer:

1. Which videos generate the highest views?
2. Which videos receive the most likes?
3. Which videos generate the most comments?
4. How does performance change by year?
5. How does performance vary by month?
6. Is there a relationship between likes and comments?
7. Which videos consistently appear among top-performing content?
8. How does individual video performance compare with overall channel performance?

## Refresh Workflow

```text
YouTube Data API
       ↓
Python Extraction
       ↓
PostgreSQL Update
       ↓
SQL Analysis
       ↓
Power BI Refresh
       ↓
Updated Dashboard
```

## Recommended GitHub Structure

```text
youtube-channel-analytics/
│
├── python/
│   ├── channel_data.py
│   └── video_data.py
│
├── sql/
│   ├── schema.sql
│   ├── analysis.sql
│   └── views.sql
│
├── powerbi/
│   └── youtube_analytics_dashboard.pbix
│
├── screenshots/
│   └── youtube_analytics_dashboard.png
│
├── documentation/
│   └── YouTube_Analytics_Project_Report.pdf
│
├── .env.example
├── .gitignore
└── README.md
```

## GitHub Upload Checklist

Upload:

- README.md
- Python scripts
- SQL scripts
- Power BI PBIX file, if appropriate for sharing
- Dashboard screenshot
- Project PDF report
- `.env.example`

Never upload:

- `.env`
- Real API key
- Database passwords
- Private credentials

## Skills Demonstrated

- YouTube Data API v3
- Python
- VS Code
- PostgreSQL
- SQL
- Data transformation
- Data modeling
- DAX
- Power BI
- Dashboard design
- KPI development
- Data visualization
- Business analysis
- GitHub
- API credential security

## Conclusion

This project demonstrates a complete real-data analytics workflow from API extraction to Business Intelligence reporting.

YouTube Data API v3, Python, PostgreSQL, SQL, and Power BI are combined to convert channel and video statistics into an interactive dashboard covering content reach, audience engagement, publishing trends, and channel performance.

**Project:** YouTube Channel Analytics Dashboard  
**Channel:** Regaltos  
**Handle:** @soulregaltos9810  
**Stack:** YouTube Data API v3 → Python → PostgreSQL → SQL → Power BI
