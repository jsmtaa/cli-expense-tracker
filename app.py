import os
class App:
    def __init__(self, accounts, ui):
        self.accounts = accounts
        self.ui = ui

    def run(self):
        while True:
            self.ui._clear_display()
            self.ui.display_actions()
            action = self.ui.get_action()
            
            match action:
                case 0: # Exit App
                    return
                case 1:
                    self.expense_service()
                case 2: 
                    self.income_service()
                case 3:
                    self.transfer_service()
                case 4: # Display accounts
                    self.ui.display_accounts(self.accounts)
                case _: # Exception
                    raise ValueError

            self.ui.prompt_before_next_action()

    # Services
    def expense_service(self):
        expense_amount = self.ui.get_expense()
        source_account = self.get_account("expense")
        if expense_amount > source_account["balance"]:
            raise ValueError("You don't have enough balance!")
        source_account["balance"] -= expense_amount

        self.ui._clear_display()
        self.ui.display_updated_balance(source_account, "expense")
    
    def income_service(self):
        income_amount = self.ui.get_income()
        destination_account = self.get_account("income")
        destination_account["balance"] += income_amount

        self.ui._clear_display()
        self.ui.display_updated_balance(destination_account)
    
    def transfer_service(self):
        # Process transfer
        source_account, destination_account = self.get_account("transfer")
        transfer_amount = self.ui.get_transfer_amount()
        if transfer_amount > source_account["balance"]:
            print("Not enough funds!")
            raise ValueError
        source_account["balance"] -= transfer_amount
        destination_account["balance"] += transfer_amount
        # Display updated accounts balance
        self.ui._clear_display()
        self.ui.display_updated_balance(source_account, destination_account, "transfer")

    def get_account(self, path):
        account = self.ui._select_account(self.accounts, path)
        return account

