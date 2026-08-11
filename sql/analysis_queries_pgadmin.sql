============================================
-- Query 1: Count Total Videos
-- Description: Displays the total number of videos
-- ============================================

SELECT COUNT(*) AS total_videos
FROM videos;

 ============================================
-- Query 2: Top 10 Most Viewed Videos
-- Description: Displays the 10 videos with the highest views
-- ============================================

SELECT
    title,
    views
FROM videos
ORDER BY views DESC
LIMIT 10;

============================================
-- Query 3: Top 10 Most Liked Videos
-- Description: Displays the 10 videos with the highest likes
-- ============================================

SELECT
    title,
    likes
FROM videos
ORDER BY likes DESC
LIMIT 10;

============================================
-- Query 4: Top 10 Most Commented Videos
-- Description: Displays the 10 videos with the highest comments
-- ============================================

SELECT
    title,
    comments
FROM videos
ORDER BY comments DESC
LIMIT 10;

-- ============================================
-- Query 5: Videos Uploaded Each Year
-- Description: Shows how many videos were uploaded each year
-- ============================================

SELECT
    EXTRACT(YEAR FROM published_at) AS year,
    COUNT(*) AS total_videos
FROM videos
GROUP BY year
ORDER BY year;

- ============================================
-- Query 6: Average Views, Likes and Comments
-- Description: Shows the average performance of videos
-- ============================================

SELECT
    ROUND(AVG(views), 2) AS average_views,
    ROUND(AVG(likes), 2) AS average_likes,
    ROUND(AVG(comments), 2) AS average_comments
FROM videos;

 ============================================
-- Query 7: Videos with Above-Average Views
-- Description: Finds videos that have more views than the average
-- SQL Concepts: Subquery, WHERE, AVG(), ORDER BY
-- ============================================

SELECT
    title,
    views
FROM videos
WHERE views > (
    SELECT AVG(views)
    FROM videos
)
ORDER BY views DESC;

============================================
-- Query 8: Top 10 Videos by Engagement Rate
-- Description: Calculates engagement rate for each video
-- SQL Concepts: Arithmetic Operations, NULLIF(), ROUND(), ORDER BY
-- ============================================

SELECT
    title,
    views,
    likes,
    comments,
    ROUND(
        ((likes + comments)::NUMERIC / NULLIF(views, 0)) * 100,
        2
    ) AS engagement_rate
FROM videos
ORDER BY engagement_rate DESC
LIMIT 10;

============================================
-- Query 9: Channel Summary
-- Description: Joins channels and videos tables
-- SQL Concepts: INNER JOIN, GROUP BY, COUNT()
-- ============================================

SELECT
    c.channel_name,
    c.subscribers,
    c.total_views,
    c.total_videos,
    COUNT(v.video_id) AS videos_in_database
FROM channels c
INNER JOIN videos v
ON c.channel_id = v.channel_id
GROUP BY
    c.channel_name,
    c.subscribers,
    c.total_views,
    c.total_videos;

- ============================================
-- Query 10: Monthly Upload Trend
-- Description: Displays the number of videos uploaded each month
-- SQL Concepts: DATE_TRUNC(), GROUP BY, ORDER BY
-- ============================================

SELECT
    DATE_TRUNC('month', published_at) AS upload_month,
    COUNT(*) AS total_uploads
FROM videos
GROUP BY upload_month
ORDER BY upload_month;