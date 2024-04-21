import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "library_management"
)
mycursor = mydb.cursor()
sql = "insert into books(Number_of_books, Book_name, Quantity, price, Author_name) VALUES (%s, %s, %s, %s, %s)"
val = ('1', "The Guns of august", "1", "99", "Barbara")
mycursor.execute(sql, val)
mydb.commit()
print("Data inserted successfully")
'''mycursor.execute("Create table books(Number_of_books int(2) PRIMARY KEY AUTO_INCREMENT, Book_name varchar(155), Quantity varchar(155), price varchar(10), Author_name varchar(120))")
print("Database created successfully.")'''