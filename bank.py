import random
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="bankdb"
)
cursor = conn.cursor()

# cursor.execute("create database bankdb1")
# cursor.execute("CREATE TABLE accounts (acc_no varchar(10),username varchar(100),balance int)")

accounts = {}

def acc_no():
    return str(random.randint(100000, 999999))

def create_account():
    username = input("Enter your username: ")
    balance = int(input("Enter initial balance: "))
    acct_no = acc_no()
    accounts[acct_no] = {"username": username, "balance": balance}
    print(f"\nAccount created successfully!\nAccount Number: {acct_no}")
    transaction_menu(username, acct_no)

def verify_account():
    username = input("Enter your username: ")
    acct_no = input("Enter your account number: ")
    if acct_no in accounts and accounts[acct_no]["username"] == username:
        print(f"\nWelcome back, {username}")
        transaction_menu(username, acct_no)
    else:
        print("Error: Invalid username or account number!")

def deposit(username, acct_no):
    amount = int(input("Enter amount to deposit: "))
    accounts[acct_no]["balance"] += amount
    print(f"Deposit successful. New balance: {accounts[acct_no]['balance']}")

def withdraw(username, acct_no):
    amount = int(input("Enter amount to withdraw: "))
    if amount <= accounts[acct_no]["balance"]:
        accounts[acct_no]["balance"] -= amount
        print(f"Withdrawal successful. New balance: {accounts[acct_no]['balance']}")
    else:
        print("Error: Insufficient balance!")

def delete_account(username, acct_no):
    confirm = input("Are you sure you want to delete this account? (yes/no): ")
    if confirm.lower() == 'yes':
        del accounts[acct_no]
        print("Account deleted successfully.")
    else:
        print("Deletion cancelled.")

def transaction_menu(username, acct_no):
    while True:
        print("\n--- Transaction Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Delete Account")
        print("4. Return to Main Menu")
        print("5. Exit and Save to MySQL")
        choice = input("Enter your choice: ")

        if choice == '1':
            deposit(username, acct_no)
        elif choice == '2':
            withdraw(username, acct_no)
        elif choice == '3':
            delete_account(username, acct_no)
            break
        elif choice == '4':
            main_menu()
            break
        elif choice == '5':
            save_table()
            print("Data saved. Exiting.")
            exit()
        else:
            print("Invalid choice. Try again.")

def main_menu():
    while True:
        print("\n--- Bank Management System ---")
        print("1. Create Account")
        print("2. Existing User Login")
        print("3. Exit and Save to MySQL")
        choice = input("Enter your choice: ")

        if choice == '1':
            create_account()
        elif choice == '2':
            verify_account()
        elif choice == '3':
            save_table()
            print("Data saved. Exiting.")
            break
        else:
            print("Invalid choice. Try again.")

def save_table():
    for acct_no, data in accounts.items():
        cursor.execute("INSERT INTO accounts (acc_no, username, balance) VALUES (%s, %s, %s)",(acct_no, data["username"], data["balance"]))
    conn.commit()
    print("All accounts saved")

main_menu()