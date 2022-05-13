import mysql.connector as db
from mysql.connector import Error


connection = db.connect(
    host='localhost', 
    database='comics', 
    user='root', 
    password='root')
   
db_Info = connection.get_server_info()
print("Connected to MySQL Server version ", db_Info)
insert = connection.cursor()
q = "INSERT INTO charact (id, name, weapon, studio_id) VALUES (NULL, %s, %s, %s)"
s = ("Petr","Kozak", 1)
n = str(input("vlož do tabulky jmeno: "))
w = str(input("zbran:"))
id = int(input("id:"))
insert.execute(q, (n,w,id))
connection.commit()
