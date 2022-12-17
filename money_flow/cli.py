from prettytable.colortable import ColorTable, Theme
from money import MoneyManager

money_manager = MoneyManager()

class CliManager:

    valid_inputs = {
        "ami": "add money income",
        "amo": "add money outcome",
        "vm": "view money",
        "dm": "delete money",
        "um": "update money",
        "q": "quit from application"
    }

    table_color_theme = Theme(
        default_color="96",
        vertical_color="20",
        horizontal_color="56",
        junction_color="36",
    )

    def show_input_table(self):
        input_table = ColorTable(theme=self.table_color_theme)
        input_table.field_names = ["action", "value"]
        input_table.border = True

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
        table = ColorTable(theme=self.table_color_theme)
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
        self.view_money()

        transaction_id = input("please enter transaction id that you want to delete ?")
        money_manager.delete(transaction_id)

        self.view_money()

    def update_money(self):
        self.view_money()
        money_id = input("please enter transaction id that you want to update ?")
        print(
            "please enter the fields that you want update ? "
            "fields: amount, status, date, description."
        )
        update_col_input = input()
        update_columns = update_col_input.split(",")
        updated_values = {}

        for each_input in update_columns:
            updated_values[each_input] = input(f"{each_input}:")

        money_manager.update(money_id, updated_values)
        print("successfully updated")

    def quit_application(self):
        exit()

