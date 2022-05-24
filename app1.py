
import mysql.connector

dataBase = mysql.connector.connect(
host ="localhost",
user ="prakash",
passwd ="Prakash@1211",
database = "sample_db"
)

# preparing a cursor object
cursorObject = dataBase.cursor()
 
# creating database
# cursorObject.execute("CREATE DATABASE sample_db")

studentRecord = """CREATE TABLE parking (
                   pid INT NOT NULL,
                   pnm VARCHAR(50),
                   level INT NOT NULL,
                   freespace VARCHAR(5),
                   vehicleno VARCHAR(50),
                   nod INT NOT NULL,
                   payment VARCHAR(50)
                   )"""

vehicleRecord = """CREATE TABLE vehicle (
                   pid INT NOT NULL,
                   vnm VARCHAR(50),
                 
                   dateofpur VARCHAR(50)
                  
                   )"""
  
# table created
cursorObject.execute(vehicleRecord)

# sql = "INSERT INTO STUDENT (NAME, BRANCH, ROLL, SECTION, AGE)\
# VALUES (%s, %s, %s, %s, %s)"
# val = [("Nikhil", "CSE", "98", "A", "18"),
#        ("Nisha", "CSE", "99", "A", "18"),
#        ("Rohan", "MAE", "43", "B", "20"),
#        ("Amit", "ECE", "24", "A", "21"),
#        ("Anil", "MAE", "45", "B", "20"),
#        ("Megha", "ECE", "55", "A", "22"),
#        ("Sita", "CSE", "95", "A", "19")]
   
# cursorObject.executemany(sql, val)

# query = "SELECT NAME, ROLL FROM STUDENT"
# cursorObject.execute(query)
   
# myresult = cursorObject.fetchall()
   
# for x in myresult:
#     print(x)
 
dataBase.commit()
# print(dataBase)
dataBase.close()
