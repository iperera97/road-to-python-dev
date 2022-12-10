from config import cursor, connection


class MoneyManager:

    def create(self, status, description, date, amount):
        cursor.execute(
            "INSERT INTO transactions (description, status, date, amount) VALUES (?, ?, ?, ?)",
            (description, status, date, amount)
        )
        connection.commit()
        return True
    
    def read(self):
        cursor.execute(
            "SELECT id, description, status, date, amount from transactions;"
        )
        return cursor.fetchall()

    def delete(self):
        pass

    def update(self):
        pass
