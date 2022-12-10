from prettytable import PrettyTable
from money import MoneyManager

money_manager = MoneyManager()

class CliManager:

    valid_inputs = {
        "ami": "add money income",
        "amo": "add money outcome",
        "vm": "view money"
    }

    def show_input_table(self):
        input_table = PrettyTable()
        input_table.field_names = ["action", "value"]

        for key, value in self.valid_inputs.items():
            input_table.add_row([key, value])

        print(input_table)

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
        date = input("date :- ")
        description = input("description :- ")
        amount = input("amount :- ")
        status = "outcome"

        result = money_manager.create(status, description, date, amount)
        print("result, ", result)

    def view_money(self):
        result = money_manager.read()
        table = PrettyTable()
        table.field_names = ["id", "date", "description", "income", "outcome", "saving"]
        total_income = 0
        total_outcome = 0

        for each in result:
            status = each["status"]
            income_amount = 0
            outcome_amount = 0

            if status == "income":
                income_amount = each["amount"]
                total_income += income_amount
            elif status == "outcome":
                outcome_amount = each["amount"]
                total_outcome += outcome_amount

            # each rows
            table.add_row([
                each["id"], each["date"], each["description"],
                income_amount, outcome_amount, income_amount - outcome_amount
            ])

        # final row
        table.add_row([
            "", "", "Summary", total_income,
            total_outcome, total_income - total_outcome
        ])
        print(table)

    def delete_money(self):
        pass

    def update_money(self):
        pass


