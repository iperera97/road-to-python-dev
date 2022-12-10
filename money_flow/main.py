from cli import CliManager


cli_manager = CliManager()


if __name__ == "__main__":
    print("please enter your input.")
    cli_manager.show_input_table()

    user_input = input()
    if cli_manager.validate_input(user_input):

        methods = {
            "ami": cli_manager.add_money_income,
            "amo": cli_manager.add_money_outcome,
            "vm": cli_manager.view_money
        }

        methods[user_input]()