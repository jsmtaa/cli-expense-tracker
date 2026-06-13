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
            elif action == 3:
                source, destination, amount = self.transfer()
            else:
                raise ValueError
            if action != 3:
                print(f"Your updated balance for account \"{account["name"]}\" is {account["balance"]}")
            else:
                print(f"Successfully transferred {amount} from {source["name"]} to {destination["name"]}.")
                print("Your updated balance:")
                print(f"\"{source["name"]}\": \"{source["balance"]}\"")
                print(f"\"{destination["name"]}\": \"{destination["balance"]}\"")

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
    
    def transfer(self):
        source_account = self.get_account()
        destination_account = self.get_account()
        amount = self.ui.get_transfer_amount()
        if amount > source_account["balance"]:
            print("Not enough funds!")
            raise ValueError
        source_account["balance"] -= amount
        destination_account["balance"] += amount
        return source_account, destination_account, amount

    def get_account(self):
        account = self.ui.select_account(self.accounts)
        return account

