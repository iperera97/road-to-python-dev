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

    def update(self, transaction_id, update_data):
        query = f"UPDATE {self.table_name} SET "
        counter = 1
        item_count = len(update_data)

        for key, _ in update_data.items():
            if counter == item_count:
                query += f"{key} = ?"
            else:
                query += f"{key} = ?,"

            counter += 1
        
        query += f" where id = {transaction_id}"

        cursor.execute(query, list(update_data.values()))
        connection.commit()
        return True


