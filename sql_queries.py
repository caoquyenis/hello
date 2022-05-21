# DROP TABLES

songsplays_table_drop = "DROP TABLE IF EXISTS songsplays"
users_table_drop = "DROP TABLE IF EXISTS users"
songs_table_drop = "DROP TABLE IF EXISTS songs"
artists_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songsplays_table_create = """CREATE TABLE IF NOT EXISTS songsplays (songsplay_id varchar,start_time float,user_id varchar,level varchar,song_id varchar,artists_id varchar,session_id varchar,location varchar,user_agent varchar);"""

users_table_create = """CREATE table if not exists users (user_id varchar,first_name varchar,last_name varchar,gender varchar,level varchar);"""

songs_table_create = """CREATE table if not exists songs (song_id varchar,title varchar,artist_id varchar,year int,duration float);"""

artists_table_create = """CREATE table if not exists artists (artist_id varchar,artist_name varchar,artist_location varchar,artist_latitude float,artist_longitude float);
"""

time_table_create = """CREATE table if not exists time (start_time float,hour int,day int,week int,month int,year int,weekday int);"""

# INSERT RECORDS

songsplays_table_insert = ("""INSERT INTO songsplays (start_time, user_id, level, song_id, artists_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""")

users_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s)""")

songs_table_insert = ("""INSERT INTO songs(song_id, artist_id, year, duration) VALUES (%s, %s, %s, %s)""")
# Select columns for artist ID, name, location, latitude, and longitude
artists_table_insert = ("""INSERT INTO artists (artist_id, artist_name, artist_location, artist_latitude, artist_longitude) VALUES (%s, %s, %s, %s, %s)""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)""")

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