import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "recipe_management"
)
mycursor = mydb.cursor()
sql = "insert into recipe(number_of_recipes, food_name, quantity, ingredients, chef_name) VALUES (%s, %s, %s, %s, %s)"
val = ('1', "Biryani", "250gn", "Vegetables", "rash")
mycursor.execute(sql, val)
mydb.commit()
print("Data inserted successfully")
'''mycursor.execute("Create table recipe(number_of_recipes int(2) PRIMARY KEY AUTO_INCREMENT, food_name varchar(155), quantity varchar(155), ingredients varchar(10), chef_name varchar(120))")
print("Database created successfully.")'''