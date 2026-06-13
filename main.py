from ui import UI
from app import App

def main():
    accounts = {
            "001": {
                "name": "Cash",
                "type": "debit",
                "balance": 1000.0
            },
            "002": {
                "name": "GCash",
                "type": "debit",
                "balance": 97.0
            },
            "003": {
                "name": "GoTyme",
                "type": "savings",
                "balance": 97.0
            }
        }

    ui = UI()
    app = App(accounts, ui)
    
    app.run()
    
if __name__ == "__main__":
    main()
