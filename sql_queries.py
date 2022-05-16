# DROP TABLES

songsplays_table_drop = "DROP TABLE IF EXISTS songsplays"
users_table_drop = "DROP TABLE IF EXISTS users"
songs_table_drop = "DROP TABLE IF EXISTS songs"
artists_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songsplays_table_create = """CREATE TABLE IF NOT EXISTS songsplays (songsplay_id int,start_time float,user_id int,level int,song_id int,artists_id int,session_id int,location varchar,user_agent varchar);"""

users_table_create = """CREATE table if not exists users (user_id int,first_name varchar,last_name varchar,gender varchar,level int);"""

songs_table_create = """CREATE table if not exists songs (songs_id int,title varchar,artists_id int,year int,duration float);"""

artists_table_create = """CREATE table if not exists artists (artists_id int,name varchar,location varchar,latitube float,longitude float);
"""

time_table_create = """CREATE table if not exists time (start_time float,hour int,day int,week int,month int,year int,weekday int);"""

# INSERT RECORDS

songsplays_table_insert = ("""
""")

users_table_insert = ("""
""")

songs_table_insert = (""""INSERT INTO songs (song_id, artist_id, year, duration) \
                 VALUES (%s, %s, %s, %s)"
""")
# Select columns for artist ID, name, location, latitude, and longitude
artists_table_insert = (""""INSERT INTO artists (artist_id, name, location, latitude, longitude) \
                 VALUES (%s, %s, %s, %s, %s)"
""")


time_table_insert = ("""
""")

# FIND songs

songs_select = ("""
""")

# QUERY LISTS

create_table_queries = [songsplays_table_create, users_table_create, songs_table_create, artists_table_create, time_table_create]
drop_table_queries = [songsplays_table_drop, users_table_drop, songs_table_drop, artists_table_drop, time_table_drop]