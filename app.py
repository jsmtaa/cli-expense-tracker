class App:
    def __init__(self, accounts, ui):
        self.accounts = accounts
        self.ui = ui

    def run(self):
        while True:
            action = self.ui.get_action()
            if action == 0:
                return
            elif action == 1:
                account = self.log_expense()
            elif action == 2:
                account = self.log_income()   
            else:
                raise ValueError
            print(f"Your updated balance for account \"{account["name"]}\" is {account["balance"]}")

    def log_expense(self):
        expense = self.ui.get_expense()
        account = self.get_account()
        if expense > account["balance"]:
            raise ValueError("You don't have enough balance!")
        account["balance"] -= expense
        return account

    def log_income(self):
        income = self.ui.get_income()
        account = self.get_account()
        account["balance"] += income
        return account

    def get_account(self):
        account = self.ui.select_account(self.accounts)
        return account

