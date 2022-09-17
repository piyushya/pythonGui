import sqlite3
db = sqlite3.connect("data.db")

try :
    curr = db.cursor()
    curr.execute("DROP TABLE IF EXISTS user")
    # Creating table
    query = """ CREATE TABLE user (
                userID INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(64) NOT NULL UNIQUE,
                email VARCHAR(120) UNIQUE,
                hash VARCHAR(128) NOT NULL
            ); """
    curr.execute(query)
    print("Database Reset Succesfull")

except :
    print ('Error in Operation')
    db.rollback()
db.close()