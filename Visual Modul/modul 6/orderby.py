import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306",
    database="db_penjualan"
)

mycursor = mydb.cursor()
sql = "select * from kategori order by nama"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)