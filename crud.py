import mysql.connector


# Connect to the database server
try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user = 'root',
        password = 'Kaynat@73',
        database = 'indigo'
    )
    mycursor = conn.cursor()
    print("Connection established")
except:
    print("connection error!")

# create a database on the db server
# mycursor.execute("CREATE DATABASE indigo")
# conn.commit()

# create a table
# Airport -> airport_id / code / name

# mycursor.execute("""
# CREATE TABLE airport(
#     airport_id INTEGER PRIMARY KEY ,
#     code VARCHAR(10) NOT NULL ,
#     city VARCHAR(255) NOT NULL
# )
# """)
# conn.commit()

# mycursor.execute("""
# ALTER TABLE airport
# ADD name VARCHAR(255) NOT NULL
# """)
# conn.commit()

# Insert data to table
# mycursor.execute("""
# INSERT INTO airport VALUES
#     (1,'DEL','New Delhi', 'IGIA'),
#     (2,'CCU','Kolkata','NSCA'),
#     (3,'BOM','Mumbai','CSMA')
# """)
# conn.commit()

# search / Retrive
mycursor.execute("SELECT * FROM airport WHERE airport_id>1")
data = mycursor.fetchall()
print(data)

for i in data:
    print(i[3])


# update
mycursor.execute("""
UPDATE airport 
SET name = 'Bombay'
WHERE airport_id = 3
""")
conn.commit()

mycursor.execute("SELECT * FROM airport ")
data = mycursor.fetchall()
print(data)

# DELETE
mycursor.execute("DELETE FROM airport WHERE airport_id = 3")
conn.commit()

mycursor.execute("SELECT * FROM airport ")
data = mycursor.fetchall()
print(data)