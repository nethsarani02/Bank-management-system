# Function to create a new account
def create_account(accounts, acc_number,balance):
    # Check whether the account number already exists
    if acc_number in accounts:
        print("Your account is already exists")
    else:
    #create  a  new  account
        accounts[acc_number] = balance
        print(f"Account created successfully with account number {acc_number}")

#Deposit  Function to deposit money
def deposit(accounts, acc_number, amount):
# Check whether  the deposit amount is positive
    if amount < 0:
        print("Deposit amount must be positive")
    else:
        if acc_number in accounts:
            # Adding  the deposit money to the balance
            accounts[acc_number] += amount
            print(f"Deposit of Rs.{amount} successful. New balance: Rs.{accounts[acc_number]}")
        else:
            print("Your account not found")

#funtion to withdraw money
def withdraw(accounts, acc_number, amount):
    if amount < 0:
        #check whether  withdraw amount is  positive  or  not
        print("Withdrawal amount must be positive")
    else:
        if acc_number in accounts:
            if amount > accounts[acc_number]:
                print("Insufficient funds")
            else:
                #Reduce account balance by withdrawal  amount.
                accounts[acc_number] -= amount
                print(f"Withdrawal of Rs.{amount} successful. New balance: Rs.{accounts[acc_number]}")
        else:
            print("Your account not found")

#function  to transfer  the  money
def transfer(accounts, acc_number1, acc_number2, amount):
    #check whether transfer amount positive or not
    if amount < 0:
        print("Transfer amount must be positive")
    else:
        if acc_number1 in accounts and acc_number2 in accounts:
            if amount > accounts[acc_number1]:
                print("Insufficient funds")
            else:
                #Reduce the transfer amount from the  account1 and add it to the  account2
                accounts[acc_number1] -= amount
                accounts[acc_number2] += amount
                print(f"Transfer of Rs{amount} successful from {acc_number1} to {acc_number2}")
        else:
            print("Accounts not found")

#function  for check  the  balance
def check_balance(accounts, acc_number):
    if acc_number in accounts:
        print(f"Account balance: Rs.{accounts[acc_number]}")
    else:
        print("Your account not found")

#main  functions  for get  inputs  from  user
def main():
    accounts = {}

    while True:
        print(" 1.Create Account 2.Deposit 3.Withdraw 4.Check Balance 5.Transfer 6.Exit")
        choice = input("Enter your choice: ")

        if choice == '1.Create Account':
            acc_number = input("Enter account number: ")
            balance = float(input("Enter the balance:"))
            create_account(accounts, acc_number, balance)

        elif choice == '2.Deposit':
            acc_number = input("Enter account number: ")
            amount = float(input("Enter deposit amount: "))
            deposit(accounts, acc_number, amount)

        elif choice == '3.Withdraw':
            acc_number = input("Enter account number: ")
            amount = float(input("Enter withdrawal amount: "))
            withdraw(accounts, acc_number, amount)

        elif choice == '4.Check Balance':
            acc_number = input("Enter account number: ")
            check_balance(accounts, acc_number)

        elif choice == '5.Transfer':
            acc_number1 = input("Enter source account number: ")
            acc_number2 = input("Enter transfering account number: ")
            amount = float(input("Enter transfer amount: "))
            transfer(accounts, acc_number1, acc_number2, amount)

        elif choice == '6.Exit':
            print("Exiting!")
            break

        else:
            print("Invalid choice ! Please choose a  valid  choice")


if __name__ == "__main__":
    main()
