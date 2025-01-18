import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306",
    database="db_penjualan"
)

mycursor = mydb.cursor()
sql = "delete from kategori where id = '4'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")