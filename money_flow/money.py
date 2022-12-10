from config import cursor, connection


class MoneyManager:

    table_name = "transactions"

    def create(self, status, description, date, amount):
        cursor.execute(
            f"INSERT INTO {self.table_name} (description, status, date, amount) VALUES (?, ?, ?, ?)",
            [description, status, date, amount]
        )
        connection.commit()
        return True
    
    def read(self):
        cursor.execute(
            f"SELECT id, description, status, date, amount from {self.table_name};"
        )
        return cursor.fetchall()

    def delete(self, transaction_id):
        cursor.execute(
            f"DELETE FROM {self.table_name} WHERE id = ?",
            [transaction_id]
        )
        connection.commit()
        return True

    def update(self):
        pass
