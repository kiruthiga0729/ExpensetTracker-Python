# from mysql.connector import connection
# myexp = connection.MySQLConnection(
# user='root',
# password='root',
# host='localhost',
# )
# mycursor = myexp.cursor()
# mycursor.execute("CREATE DATABASE expense_db")


from mysql.connector import connection
myexp = connection.MySQLConnection(
user='root',
password='root',
host='localhost',
database="expense_db"
)
mycursor = myexp.cursor()

# mycursor.execute("""
#     CREATE TABLE category (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         name VARCHAR(100) NOT NULL,
#         description TEXT
#     )
# """)

# mycursor.execute("""
#     CREATE TABLE expense (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         name VARCHAR(100) NOT NULL,
#         amount DECIMAL(10, 2) NOT NULL,
#         date DATE NOT NULL,
#         category_id INT,
#         FOREIGN KEY (category_id) REFERENCES category(id)
#     )
# """)

# myexp.commit()
# print("Tables created successfully!")



# sql = "INSERT INTO category(name, description) VALUES (%s, %s)"
# val = [("Food", "Daily meals and snacks"),
#       ("Transport", "Bus, fuel, etc."),
#         ("Shopping", "Clothes, groceries"),
#         ("Utilities", "Electricity, water"),
#         ("Entertainment", "Movies, games"),
# ]
# mycursor.executemany(sql, val) 
# myexp.commit()
# print(mycursor.rowcount, "was inserted.") 


 
# sql = "INSERT INTO expense(name, amount, date, category_id) VALUES (%s, %s, %s, %s)" 
# val =  [
#         ("Breakfast", 50, "2025-01-03", 1),
# ("Bus fare", 20, "2025-02-07", 2),
# ("Lunch", 100, "2025-03-12", 1),
# ("Shirt", 500, "2025-04-09", 3),
# ("Electric Bill", 1200, "2025-05-05", 4),
# ("Movie", 200, "2025-07-19", 5),
# ("Snacks", 40, "2025-08-14", 1),
# ("Diesel", 800, "2025-09-21", 2),
# ("Dinner", 90, "2025-10-02", 1),
# ("Mobile Bill", 400, "2025-11-17", 4),
# ("Pizza", 300, "2025-01-24", 1),
# ("Taxi", 250, "2025-02-28", 2),
# ("Dress", 700, "2025-03-30", 3),
# ("Game", 150, "2025-04-15", 5),
# ("Groceries", 600, "2025-05-26", 3),
# ("Lunch", 120, "2025-06-22", 1),
# ("Train Ticket", 90, "2025-07-04", 2),
# ("Water Bill", 300, "2025-08-11", 4),
# ("TV Recharge", 350, "2025-09-29", 4),
# ("Ice Cream", 70, "2025-10-25", 1)
# ]
# mycursor.executemany(sql, val) 
# myexp.commit()
# print(mycursor.rowcount, "was inserted.") 



# sql = "INSERT INTO expense(name, amount, date, category_id) VALUES (%s, %s, %s, %s)" 
# val =  [("books", 150, "2025-06-11", 5)]
# mycursor.executemany(sql, val) 
# myexp.commit()
# print(mycursor.rowcount, "was inserted.")



# sql = "UPDATE expense SET amount = '250' WHERE amount = '90'" 
# mycursor.execute(sql) 
# myexp.commit() 
# print(mycursor.rowcount, "record(s) affected") 


 
# sql = "DELETE FROM expense WHERE id = '21'"
# mycursor.execute(sql) 
# myexp.commit() 
# print(mycursor.rowcount, "record(s) deleted") 


 
# sql = "SELECT * FROM expense WHERE date ='2025-06-22'" 
# mycursor.execute(sql) 
# myresult = mycursor.fetchall() 
# for x in myresult: 
#  print(x) 



# sql = "SELECT * FROM expense WHERE category_id LIKE '%1%'"
# mycursor.execute(sql) 
# myresult = mycursor.fetchall() 
# for x in myresult: 
#  print(x) 


expense = [
                ("Breakfast", 50, "2025-01-03", 1),
("Bus fare", 20, "2025-02-07", 2),
("Lunch", 100, "2025-03-12", 1),
("Shirt", 500, "2025-04-09", 3),
("Electric Bill", 1200, "2025-05-05", 4),
("Movie", 200, "2025-07-19", 5),
("Snacks", 40, "2025-08-14", 1),
("Diesel", 800, "2025-09-21", 2),
("Dinner", 90, "2025-10-02", 1),
("Mobile Bill", 400, "2025-11-17", 4),
("Pizza", 300, "2025-01-24", 1),
("Taxi", 250, "2025-02-28", 2),
("Dress", 700, "2025-03-30", 3),
("Game", 150, "2025-04-15", 5),
("Groceries", 600, "2025-05-26", 3),
("Lunch", 120, "2025-06-22", 1),
("Train Ticket", 90, "2025-07-04", 2),
("Water Bill", 300, "2025-08-11", 4),
("TV Recharge", 350, "2025-09-29", 4),
("Ice Cream", 70, "2025-10-25", 1)
]

total_expense=sum(amount for _, amount, _, _ in expense)
print(f"\ntotal expenses:{total_expense}")

category_totals={}
for name,amount,date,category in expense:
    if category in category_totals:
        category_totals[category]+=amount
    else:
        category_totals[category]=amount
print("\ncategory-wise breakdown:") 
for category,total in category_totals.items():
    print(f"{category}:{total}") 



from datetime import datetime
from collections import defaultdict

monthly_totals = defaultdict(int)
yearly_totals = defaultdict(int)

for name, amount, date_str, category in expense:
    date_obj = datetime.strptime(date_str, "%Y-%m-%d" ) 

    month_key=date_obj.strftime("%Y-%m") 
    year_key=date_obj.strftime("%Y")


    monthly_totals[month_key]+=amount
    yearly_totals[year_key] += amount
print("\nmonthly totals:") 
for month, total in sorted(monthly_totals.items()):
    print(f"{month}: {total}")

print("\nyearly totals:")
for year, total in sorted(yearly_totals.items()):
    print(f"{year}: {total}")


