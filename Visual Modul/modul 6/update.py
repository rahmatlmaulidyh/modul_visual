import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306",
    database="db_penjualan"
)

mycursor = mydb.cursor()
sql = "update kategori set nama = 'Jelly' where id = '2'"

mydb.commit()
print(mycursor.rowcount, "record(s) updated")