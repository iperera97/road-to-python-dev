from cli import CliManager


cli_manager = CliManager()


if __name__ == "__main__":
    print("please enter your input.")
    print(f"valid inputs = {CliManager.valid_inputs}")

    user_input = input()
    if cli_manager.validate_input(user_input):

        methods = {
            "ami": cli_manager.add_money_income,
            "amo": cli_manager.add_money_outcome
        }

        methods[user_input]()