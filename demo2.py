import psycopg2

try:
    conn = psycopg2.connect("host=localhost dbname=postgres user=genie password=123456")
except psycopg2.Error as e:
    print("Error: Could not make connection to the Postgres database")
    print(e)

try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: Could not get curser to the Database")
    print(e)

conn.set_session(autocommit = True)

## TO-DO: Add the database name within the CREATE DATABASE statement.
try:
    cur.execute("create database demo2")
except psycopg2.Error as e:
    print(e)

try:
    conn.close()
except psycopg2.Error as e:
    print(e)

try:
    conn = psycopg2.connect("host=localhost dbname=demo2 user=genie password=123456")
except psycopg2.Error as e:
    print(e)

try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: Could not get curser to the Database")
    print(e)

conn.set_session(autocommit=True)

## TO-DO: Finish writing the CREATE TABLE statement with the correct arguments
try:
    cur.execute("CREATE TABLE IF NOT EXISTS transactions (transaction_id int, \
        customer_name varchar, cashier_name varchar, year int);")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try:
    cur.execute("CREATE TABLE IF NOT EXISTS albums_sold (album_id int, \
        transaction_id int, album_name varchar);")
except psycopg2.Error as e:
    print("Error: Issue creating table")
    print(e)

try: 
    cur.execute("INSERT INTO transactions (transaction_id, customer_name, cashier_name, year) \
                 VALUES (%s, %s, %s, %s)", \
                 (1, "Amanda", "Sam", 2000))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO transactions (transaction_id, customer_name, cashier_name, year) \
                 VALUES (%s, %s, %s, %s)", \
                 (2, "Amanda", "Sam", 2000))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO transactions (transaction_id, customer_name, cashier_name, year) \
                 VALUES (%s, %s, %s, %s)", \
                 (3, "Toby", "Sam", 2000))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO transactions (transaction_id, customer_name, cashier_name, year) \
                 VALUES (%s, %s, %s, %s)", \
                 (4, "Max", "Bob", 2018))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO transactions (transaction_id, customer_name, cashier_name, year) \
                 VALUES (%s, %s, %s, %s)", \
                 (5, "Max", "Bob", 2018))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO albums_sold (album_id, transaction_id, album_name) \
                 VALUES (%s, %s, %s)", \
                 (1, 1, "Rubber Soul"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO albums_sold (album_id, transaction_id, album_name) \
                 VALUES (%s, %s, %s)", \
                 (2, 1, "Let it Be"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO albums_sold (album_id, transaction_id, album_name) \
                 VALUES (%s, %s, %s)", \
                 (3, 2, "My Generation"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO albums_sold (album_id, transaction_id, album_name) \
                 VALUES (%s, %s, %s)", \
                 (4, 3, "Meet the Beatles"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

try: 
    cur.execute("INSERT INTO albums_sold (album_id, transaction_id, album_name) \
                 VALUES (%s, %s, %s)", \
                 (5, 3, "Help!"))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

print("Table: transactions\n")
#Validate
try:
    cur.execute("SELECT * FROM transactions;")
except psycopg2.Error as e:
    print("Error: select *")
    print(e)

row  = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

print("\nTable: albums_sold\n")
#Validate
try:
    cur.execute("SELECT * FROM albums_sold;")
except psycopg2.Error as e:
    print("Error: select *")
    print(e)

row  = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()
cur.close()
conn.close()

`Table Name: transactions2 
column 0: transaction Id
column 1: Customer Name
column 2: Cashier Id
column 3: Year `

`Table Name: albums_sold
column 0: Album Id
column 1: Transaction Id
column 3: Album Name` 

`Table Name: employees
column 0: Employee Id
column 1: Employee Name `

`Table Name: sales
column 0: Transaction Id
column 1: Amount Spent