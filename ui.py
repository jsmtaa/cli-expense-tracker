import os 

class UI:
    # Helpers
    def _clear_display(self):
        os.system("clear")

    def _get_input(self):
        return input("> ")

    # Display
    def display_actions(self):
        print("Select an action:")
        print("1. Log expense")
        print("2. Log income")
        print("3. Transfer")
        print("4. Display accounts")
        print("0. Exit program")

    def get_action(self):
        return int(self._get_input())
    def display_updated_balance(self, first_account, second_account=None, transaction="default"):
        match transaction:
            case "default":
                print(f"Your updated balance for '{first_account["name"]}' is {first_account["balance"]:.2f}")
            case "transfer":
                print("Your updated accounts balance:")
                print(f"{first_account["name"]}: {first_account["balance"]}")
                print(f"{second_account["name"]}: {second_account["balance"]}")

    def display_account_selector(self, accounts):
        for i, account in enumerate(accounts):
            print(i+1, accounts[account]["name"])


    def _select_account(self, accounts, transaction):
        indices = []

        match transaction:
            case "expense":
                print("Select a source account")
                self.display_account_selector(accounts)
                indices.append(int(self._get_input()) - 1)
            case "income":
                print("Select a destination account")
                self.display_account_selector(accounts)
                indices.append(int(self._get_input()) - 1)
            case "transfer":
                print("Select a source account:")
                self.display_account_selector(accounts)
                indices.append(int(self._get_input()) - 1)
                print("Select a destination account:")
                self.display_account_selector(accounts)
                indices.append(int(self._get_input()) - 1)

        
        result = []
        for index in indices:
            for i, account in enumerate(accounts):
                if i != index:
                    continue
                result.append(accounts[account])
        
        return result[0] if len(result) == 1 else result

    def get_expense(self):
        return float(input("Enter expense: "))

    def get_income(self):
        return float(input("Enter income: "))

    def get_transfer_amount(self):
        return float(input("Enter amount to transfer: "))

    def display_accounts(self, accounts):
        print("ACTIVE ACCOUNTS")
        for account_id in accounts:
            account = accounts[account_id]
            print(f"\n{account["name"]} | {account["type"].capitalize()}")
            print(f"AMT: {account["balance"]}")

    def display_balance(self, balance):
        print(f"Your balance is: {balance}")

    def prompt_before_next_action(self):
        input("\nPress anything to continue...")
