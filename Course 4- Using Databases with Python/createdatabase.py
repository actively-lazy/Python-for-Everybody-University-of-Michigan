import sqlite3
import random
conn = sqlite3.connect("Databases/database.sqlite")
cur = conn.cursor()

# # Uncomment to create new data base with ~5000 names
# cur.execute("DROP TABLE IF EXISTS Users")
#
# cur.execute(
#     "CREATE TABLE Users (Name TEXT,Email TEXT,Age INTEGER, Salary INTEGER)")
# for line in open("names.txt"):
#     name = line.strip()
#     email = name[0:name.find(" ")].lower() + \
#         "." + name[name.find(" ") + 1:].lower() + "@gmail.com"
#     age = random.randint(18, 61)
#     salary = random.randint(10000, 1000000)
#     cur.execute("INSERT INTO Users (Name,Email,Age,Salary) VALUES (?,?,?,?)",
#                 (name, email, age, salary))
# conn.commit()
#
for row in cur.execute("SELECT * FROM Users ORDER BY Salary  "):
    print("{:20}{:20}{:5}{:20}".format(row[0], row[1], row[2], row[3]))
