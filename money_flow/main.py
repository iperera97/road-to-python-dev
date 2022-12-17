from cli import CliManager


cli_manager = CliManager()


if __name__ == "__main__":

    while True:
        print("please enter your input.")
        cli_manager.show_input_table()
        user_input = input()
        if cli_manager.validate_input(user_input):

            methods = {
                "ami": cli_manager.add_money_income,
                "amo": cli_manager.add_money_outcome,
                "vm": cli_manager.view_money,
                "dm": cli_manager.delete_money,
                "um": cli_manager.update_money,
                "q": cli_manager.quit_application,
            }

            print("-" * 100)
            methods[user_input]()
            print("-" * 100)