import mysql.connector

db = mysql.connector.connect(
    host='197.25.216.118',
    user="root",
    passwd="Moadhos890!!",
    auth_plugin='mysql_native_password',
    database="testdatabaselol" 
)

# mycursor = db.cursor()

# # mycursor.execute("DROP TABLE Person")
# # mycursor.execute("CREATE TABLE Person (personID INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), age SMALLINT UNSIGNED)")

# mycursor.execute("INSERT INTO Person (name, age) VALUES (%s, %s)", ("Ahmed", 20))
# db.commit()

# mycursor.execute("SELECT * FROM Person")

# for x in mycursor:
#     print(x)
