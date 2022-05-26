# DROP TABLES

songsplays_table_drop = "DROP TABLE IF EXISTS songsplays"
users_table_drop = "DROP TABLE IF EXISTS users"
songs_table_drop = "DROP TABLE IF EXISTS songs"
artists_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songsplays_table_create = ("""
CREATE TABLE IF NOT EXISTS songsplays (
    songsplay_id SERIAL PRIMARY KEY NOT NULL,
    start_time BIGINT NOT NULL,
    user_id INT NOT NULL,
    level VARCHAR,
    song_id VARCHAR,
    artist_id VARCHAR,
    session_id VARCHAR,
    location VARCHAR,
    user_agent VARCHAR)
""")

users_table_create = ("""
CREATE TABLE IF NOT EXISTS users (
    user_id INT PRIMARY KEY NOT NULL,
    first_name VARCHAR,
    last_name VARCHAR,
    gender VARCHAR,
    level VARCHAR)
""")

songs_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
    song_id VARCHAR PRIMARY KEY NOT NULL,
    title TEXT NOT NULL,
    artist_id VARCHAR NOT NULL,
    year INT,
    duration FLOAT NOT NULL)
""")

artists_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
    artist_id VARCHAR PRIMARY KEY NOT NULL,
    artist_name VARCHAR NOT NULL,
    artist_location VARCHAR,
    artist_latitude FLOAT,
    artist_longitude FLOAT)
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
    start_time BIGINT PRIMARY KEY NOT NULL,
    hour INTEGER,
    day INTEGER,
    week INTEGER,
    month INTEGER,
    year INTEGER,
    weekday INTEGER)
""")

# INSERT RECORDS

songsplays_table_insert = ("""
INSERT INTO songsplays (
    start_time, 
    user_id, 
    level, 
    song_id, 
    artist_id, 
    session_id, 
    location, 
    user_agent) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

users_table_insert = ("""
INSERT INTO users (
    user_id, 
    first_name, 
    last_name, 
    gender, 
    level) 
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id) DO UPDATE SET level=EXCLUDED.level
""")

songs_table_insert = ("""
INSERT INTO songs (
    song_id, 
    title,
    artist_id, 
    year, 
    duration) 
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id) DO NOTHING
""")
# Select columns for artist ID, name, location, latitude, and longitude
artists_table_insert = ("""
INSERT INTO artists (
    artist_id, 
    artist_name, 
    artist_location, 
    artist_latitude, 
    artist_longitude) 
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id) DO NOTHING
""")


time_table_insert = ("""
INSERT INTO time (
    start_time, 
    hour, 
    day, 
    week, 
    month, 
    year, 
    weekday) 
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (start_time) DO NOTHING
""")

# FIND songs

songs_select = ("""
SELECT songs.song_id, songs.artist_id
FROM songs
INNER JOIN artists ON songs.artist_id = artists.artist_id
WHERE songs.title=%s and artists.artist_name=%s and songs.duration=%s
""")

# QUERY LISTS

create_table_queries = [songsplays_table_create, users_table_create, songs_table_create, artists_table_create, time_table_create]
drop_table_queries = [songsplays_table_drop, users_table_drop, songs_table_drop, artists_table_drop, time_table_drop]