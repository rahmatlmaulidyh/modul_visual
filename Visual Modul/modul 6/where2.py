import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    port="3306",
    database="db_penjualan"
)

mycursor = mydb.cursor()
sql = "select * from kategori where id = %s"
no = ("2",)
mycursor.execute(sql, no)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)