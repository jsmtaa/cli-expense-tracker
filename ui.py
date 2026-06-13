class UI:
    def _get_input(self):
        return input("> ")

    def get_action(self):
        print("Choose an option from the menu:")
        print("1 Log expense")
        print("2 Log income")
        print("0 Exit program")
        return int(self._get_input())

    def select_account(self, accounts):
        print("Choose an account: ")
        
        for i, account in enumerate(accounts):
            print(i+1, accounts[account]["name"])

        account_index = int(self._get_input()) - 1

        for i, account in enumerate(accounts):
            if i != account_index:
                continue
            return accounts[account]

        raise ValueError

    def get_expense(self):
        return float(input("Enter expense: "))

    def get_income(self):
        return float(input("Enter income: "))

    def display_balance(self, balance):
        print(f"Your balance is: {balance}")
