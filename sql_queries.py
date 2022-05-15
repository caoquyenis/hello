# DROP TABLES

songplay_table_drop = "Drop table songplay"
user_table_drop = "Drop table user"
song_table_drop = "Drop table song"
artist_table_drop = "Drop table artist"
time_table_drop = "Drop table time"

# CREATE TABLES

songplay_table_create = ("""Create table if not exists songplay(songplay_id int, start_time float, user_id int, level int, song_id int, artist_id int, session_id int, location varchar, user_agent varchar)
""")

user_table_create = ("""CREATE table if not exists user(user_id, first_name varchar, last_name varchar, gender varchar, level int)
""")

song_table_create = ("""CREATE table if not exists song(song_id int, title varchar, artist_id int, year int, duration num)
""")

artist_table_create = ("""CREATE table if not exists artist(artist_id int, name varchar, location varchar, latitube num, longitude num)
""")

time_table_create = ("""CREATE table if not exists time(start_time int, hour int, day int, week int, month int, year int, weekday int)
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND song

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]