class BankAccount:
    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount. Amount must be greater than 0.")
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew ${amount}. New balance: ${self.balance}")
            else:
                print("Insufficient funds for withdrawal please top-up.")
        else:
            print("Invalid withdrawal amount. Amount must be greater than 0.")
    
    def display_balance(self):
        print(f"Account holder: {self.account_holder}")
        print(f"Current balance: ${self.balance}")


if __name__ == "__main__":
    account_holder_name = input("Enter account holder's name: ")
    initial_balance = float(input("Enter initial balance: "))
    
    account = BankAccount(account_holder_name, initial_balance)
    account.display_balance()
    
    while True:
        print("\nChoose an action:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Display Balance")
        print("4. Exit")
        choice = int(input("Enter choice: "))
        
        if choice == 1:
            deposit_amount = float(input("Enter deposit amount: "))
            account.deposit(deposit_amount)
        elif choice == 2:
            withdrawal_amount = float(input("Enter withdrawal amount: "))
            account.withdraw(withdrawal_amount)
        elif choice == 3:
            account.display_balance()
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a valid option.")