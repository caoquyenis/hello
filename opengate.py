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
    cur.execute("create database demo1")
except psycopg2.Error as e:
    print(e)

try:
    conn.close()
except psycopg2.Error as e:
    print(e)

try:
    conn = psycopg2.connect("host=localhost dbname=demo1 user=genie password=123456")
except psycopg2.Error as e:
    print(e)

try:
    cur = conn.cursor()
except psycopg2.Error as e:
    print("Error: Could not get curser to the Database")
    print(e)

conn.set_session(autocommit=True)

## TO-DO: Finish writing the CREATE TABLE statement with the correct arguments
# TO-DO: Create all tables
try: 
    cur.execute("CREATE TABLE IF NOT EXISTS transactions (transaction_id int, customer_name varchar, cashier_id int, year int, amount_spent int);")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)



#Insert data into all tables 
    
try: 
    cur.execute("INSERT INTO transactions (transaction_id, customer_name, cashier_id, year, amount_spent) \
                 VALUES (%s, %s, %s, %s, %s)", \
                 (1, "Amanda", 1, 2000, 40))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO transactions (transaction_id, customer_name, cashier_id, year, amount_spent) \
                 VALUES (%s, %s, %s, %s, %s)", \
                 (2, "Toby", 1, 2000, 19))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)
    
try: 
    cur.execute("INSERT INTO transactions (transaction_id, customer_name, cashier_id, year, amount_spent) \
                 VALUES (%s, %s, %s, %s, %s)", \
                 (3, "Max", 2, 2018, 45))
except psycopg2.Error as e: 
    print("Error: Inserting Rows")
    print (e)

#Validate
try:
    cur.execute("SELECT * FROM song_lib;")
except psycopg2.Error as e:
    print("Error: select *")
    print(e)

row  = cur.fetchone()
while row:
    print(row)
    row = cur.fetchone()

cur.close()
conn.close()


try: 
    cur.execute("CREATE TABLE IF NOT EXISTS fact_table(customer_id int, store_id int, spent float);")
except psycopg2.Error as e: 
    print("Error: Issue creating table")
    print (e)