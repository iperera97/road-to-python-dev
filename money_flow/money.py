import mariadb

# create connection
connection = mariadb.connect(
    user="root",
    password="123",
    host="localhost",
    port=3306,
    database="MONEY"
)

cursor = connection.cursor(dictionary=True)

class MoneyManager:

    def create(self, status, description, date, amount):
        cursor.execute(
            "INSERT INTO transactions (description, status, date, amount) VALUES (?, ?, ?, ?)",
            (description, status, date, amount)
        )
        connection.commit()
        return True
    
    def read(self):
        pass

    def delete(self):
        pass

    def update(self):
        pass
