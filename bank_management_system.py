import os

ACCOUNT_FILE = "accounts.txt"

def create_account():
    name = input("Enter name: ")
    acc_no = input("Enter account number: ")
    acc_type = input("Enter account type (Saving/Current): ")
    balance = float(input("Enter initial deposit: "))
    
    with open(ACCOUNT_FILE, "a") as f:
        f.write(f"{acc_no},{name},{acc_type},{balance}\n")
    print("Account created successfully!")

def display_account():
    acc_no = input("Enter account number: ")
    found = False
    with open(ACCOUNT_FILE, "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == acc_no:
                print(f"Account No: {data[0]}\nName: {data[1]}\nType: {data[2]}\nBalance: {data[3]}")
                found = True
                break
    if not found:
        print("Account not found.")

def deposit_money():
    acc_no = input("Enter account number: ")
    amount = float(input("Enter amount to deposit: "))
    lines = []
    found = False
    
    with open(ACCOUNT_FILE, "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == acc_no:
                data[3] = str(float(data[3]) + amount)
                found = True
            lines.append(",".join(data))
    
    if found:
        with open(ACCOUNT_FILE, "w") as f:
            f.write("\n".join(lines) + "\n")
        print("Deposit successful!")
    else:
        print("Account not found.")

def withdraw_money():
    acc_no = input("Enter account number: ")
    amount = float(input("Enter amount to withdraw: "))
    lines = []
    found = False
    
    with open(ACCOUNT_FILE, "r") as f:
        for line in f:
            data = line.strip().split(",")
            if data[0] == acc_no:
                if float(data[3]) >= amount:
                    data[3] = str(float(data[3]) - amount)
                    found = True
                else:
                    print("Insufficient balance.")
                    return
            lines.append(",".join(data))
    
    if found:
        with open(ACCOUNT_FILE, "w") as f:
            f.write("\n".join(lines) + "\n")
        print("Withdrawal successful!")
    else:
        print("Account not found.")

def delete_account():
    acc_no = input("Enter account number to delete: ")
    lines = []
    found = False

    with open(ACCOUNT_FILE, "r") as f:
        for line in f:
            if not line.startswith(acc_no + ","):
                lines.append(line)
            else:
                found = True
    
    if found:
        with open(ACCOUNT_FILE, "w") as f:
            f.writelines(lines)
        print("Account deleted successfully.")
    else:
        print("Account not found.")

def list_accounts():
    print("\nAll Accounts:\n")
    with open(ACCOUNT_FILE, "r") as f:
        for line in f:
            data = line.strip().split(",")
            print(f"Account No: {data[0]}, Name: {data[1]}, Type: {data[2]}, Balance: {data[3]}")

def main():
    while True:
        print("\n=== Bank Management System ===")
        print("1. Create Account")
        print("2. Display Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Delete Account")
        print("6. List All Accounts")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            display_account()
        elif choice == "3":
            deposit_money()
        elif choice == "4":
            withdraw_money()
        elif choice == "5":
            delete_account()
        elif choice == "6":
            list_accounts()
        elif choice == "7":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    if not os.path.exists(ACCOUNT_FILE):
        open(ACCOUNT_FILE, "w").close()  # Create the file if it doesn't exist
    main()
