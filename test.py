## TO-DO: Query 1:  Give me the artist, song title and song's length in the music app history that was heard during \
## sessionId = 338, and itemInSession = 4
query = "CREATE TABLE IF NOT EXISTS udacity.music_library "
query = query + """(artist text, firstName text, gender text,itemSession INT,lastName TEXT,length BIGINT,level VARCHAR,location TEXT,sessionId INT,songTitle TEXT,userId INT,PRIMARY KEY(itemSession,sessionId,userId))"""
try:
    session.execute(query)
except Exception as e:
    print(e)

# We have provided part of the code to set up the CSV file. Please complete the Apache Cassandra code below#
file = 'event_datafile_new.csv'

with open(file, encoding = 'utf8') as f:
    csvreader = csv.reader(f)
    next(csvreader) # skip header
    for line in csvreader:
## TO-DO: Assign the INSERT statements into the `query` variable
        query = "INSERT INTO music_library (artist, firstname, gender, itemSession, lastName, length, level, location, sessionId, songTitle, userId)"
        query = query + "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        ## TO-DO: Assign which column element should be assigned for each column in the INSERT statement.
        ## For e.g., to INSERT artist_name and user first_name, you would change the code below to `line[0], line[1]`
        session.execute(query, (line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9], line[10]))

