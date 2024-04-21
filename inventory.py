import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "inventory_management"
)
mycursor = mydb.cursor()
sql = "insert into management(number_of_products, Name, Quantity, Date, Contact_number) VALUES (%s, %s, %s, %s, %s)"
val = ('1', "Computer", "1", "1837", "Charles")
mycursor.execute(sql, val)
mydb.commit()
print("Data inserted successfully")
'''mycursor.execute("Create table Management(number_of_products int(2) PRIMARY KEY AUTO_INCREMENT, Name varchar(155), Quantity varchar(155), Date varchar(10), Contact_Number varchar(120))")
print("Database created successfully.")'''