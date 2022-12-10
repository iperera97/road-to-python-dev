import mariadb

# create connection
connection = mariadb.connect(
    user="root",
    password="123",
    host="localhost",
    port=3306,
    database="moneyflow"
)

cursor = connection.cursor(dictionary=True)
