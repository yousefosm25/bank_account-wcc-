class BankAccount:
    def __init__(self):
        self.balance = 0
        print("Welcome to Deposit & Withdrawal Machine")

    def account(self):
        while True:
            print("\nWelcome to the Bank Account System")
            bank_pin = int(input("Bank PIN: "))
            if bank_pin == 1234:
                self.show_menu()
                break
            else:
                print("Invalid PIN. Please try again.")

    def show_menu(self):
        while True:
            print("\nPlease choose an option:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Display Balance")
            print("4. Exit")
            choice = input("Enter your choice: ")

            if choice == '1':
                self.deposit()
            elif choice == '2':
                self.withdraw()
            elif choice == '3':
                self.display_balance()
            elif choice == '4':
                print("Thank you for using the Bank Account System")
                break
            else:
                print("Invalid choice. Please try again.")

    def deposit(self):
        try:
            amount = float(input("Enter the amount to deposit: "))
            if amount <= 0:
                print("Invalid amount. Please enter a positive value.")
            else:
                self.balance += amount
                print("Deposit Successful")
                self.display_balance()
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    def withdraw(self):
        try:
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= 0:
                print("Invalid amount. Please enter a positive value.")
            elif amount > self.balance:
                print("Insufficient funds")
            else:
                self.balance -= amount
                print("Withdrawal Successful")
                self.display_balance()
        except ValueError:
            print("Invalid input. Please enter a numerical value.")

    def display_balance(self):
        print(f"Your current balance is: {self.balance}")

if __name__ == "__main__":
    account = BankAccount()
    account.account()
