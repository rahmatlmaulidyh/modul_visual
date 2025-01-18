import mysql.connector

mydb=mysql.connector.connect(host="localhost", user="root", password="", database="db_penjualan")

mycursor=mydb.cursor()
sql="INSERT INTO kategori (id,nama) VALUES (%s,%s)"
val = ("3","Snacks"),("4","Fruits"),("5","Vegetables")
mycursor.executemany(sql,val)

mydb.commit()
print(mycursor.rowcount,"Data berhasil ditambahkan")