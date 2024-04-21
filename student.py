import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "student_management"
)
mycursor = mydb.cursor()
sql = "insert into students(id, Name, Address, Phone_number, Contact_person) VALUES (%s, %s, %s, %s, %s)"
val = ('', "Faraz", "1", "Kurseong", "9992223334")
mycursor.execute(sql, val)
mydb.commit()
print("Data inserted successfully")
'''mycursor.execute("Create table students (id int(2) PRIMARY KEY AUTO_INCREMENT, Name varchar(155), Address varchar(155), Phone_number varchar(10), Contact_Person varchar(120))")
print("Database created successfully.")'''