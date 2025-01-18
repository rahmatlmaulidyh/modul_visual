import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_penjualan"
)

mycursor = mydb.cursor()
mycursor.execute("select * from kategori")
myresult = mycursor.fetchone()

for x in myresult:
    print(x)
