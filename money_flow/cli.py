from money import MoneyManager

money_manager = MoneyManager()

class CliManager:

    valid_inputs = {
        "ami": "add_money_income",
        "amo": "add_money_outcome"
    }

    def validate_input(self, input_value):
        if input_value in self.valid_inputs:
            return True
        
        print(f"invalid input please check - {self.valid_inputs}")

    def add_money_income(self):
        print("please enter below data for money income...")
        date = input("date :- ")
        description = input("description :- ")
        amount = input("amount :- ")
        status = "income"
        
        result = money_manager.create(status, description, date, amount)
        print("result, ", result)

    def add_money_outcome(self):
        print("please enter below data for money outcome...")

    def view_money(self):
        pass

    def delete_money(self):
        pass

    def update_money(self):
        pass