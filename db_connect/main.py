# 1 - install mariadb driver
# 2 - import mariadb
# 3 - connect to the database
# 4 - create a cursor (to execute query)
# 5 - execute query through cursor
# 6 - get the result
import mariadb

# connect to the database
connection = mariadb.connect(
    user="root",
    password="123",
    host="localhost",
    port=3306,
    database="studentdb"
)

# create a cursor
cursor = connection.cursor(dictionary=True)

# insert
cursor.execute(
    "INSERT INTO students (id, name, email, gender) VALUES (?, ?, ?, ?)",
    (10, 'kamal', 'v@gmail.com', False)
)
connection.commit()
###################################################

# insert many
# cursor.executemany(
#     "INSERT INTO students (id, name, email, gender) VALUES (?, ?, ?, ?)",
#     [
#         (20, 'john', 'john@gmail.com', True),
#         (30, 'jane', 'jane@gmail.com', True),
#         (40, 'wane', 'wane@gmail.com', False),
#         (50, 'Anny', 'waex@gmail.com', False)
#     ]
# )
# connection.commit()
###################################################

# update query
# cursor.execute(
#     "UPDATE students SET email = ? WHERE name = ?",
#     ('ann333@gmail.com', 'ann')
# )
# connection.commit()
###################################################

# delete query
# cursor.execute("DELETE FROM students WHERE id = ?", [20])
# connection.commit()
###################################################

# read query
# cursor.execute("SELECT id, name, email FROM students")
# print(cursor.fetchall())