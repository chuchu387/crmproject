import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'enter your password'
)

#prepare a cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE info")
print("all done")
