#Assignment 1

def encrypt_name(full_name, key):
    encrypted = ""

    for char in full_name:
        if char.isupper():
            encrypted += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        elif char.islower():
            encrypted += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
        else:
            encrypted += char 

    if key % 2 == 0:
        encrypted = encrypted[::-1]

    return encrypted

def decrypt_name(encrypted_text, key):

    if key % 2 == 0:
        encrypted_text = encrypted_text[::-1]

    decrypted = ""

    for char in encrypted_text:
        if char.isupper():
            decrypted += chr((ord(char) - ord('A') - key) % 26 + ord('A'))
        elif char.islower():
            decrypted += chr((ord(char) - ord('a') - key) % 26 + ord('a'))
        else:
            decrypted += char  

    return decrypted




full_name = input("Enter your full name: ")
first_name = full_name.split()[0]
key = len(first_name)
encrypted_text = encrypt_name(full_name, key)
decrypted_text = decrypt_name(encrypted_text, key)

print("\n🔐 Name Cipher System")
print("-" * 30)
print("Original Name :", full_name)
print("Key Used      :", key)
print("Encrypted     :", encrypted_text)
print("Decrypted     :", decrypted_text)


#Assignment 2


def print_pattern_table(n):

    print("\nMULTIPLICATION TABLES FROM 1 TO", n)
    print("-" * 40)
    for i in range(1, n + 1):
        print("\nTable of", i)

        for j in range(1, 11):
            result = i * j
            if result % 3 == 0 or result % 5 == 0 or result % 7 == 0:
                print(i, "x", j, "=", str(result) + " *")
            else:
                print(i, "x", j, "=", result)

    print("\nTRIANGLE PATTERN")
    print("-" * 40)

    for row in range(1, n + 1):
        for col in range(row):
            print("*", end=" ")
        print()

print_pattern_table(10)
print("\n" + "=" * 50)
print_pattern_table(15)



#Assignment 3

from datetime import datetime

def create_account(name, initial_balance):
    account = {
        "name": name,
        "balance": initial_balance,
        "transactions": []
    }

    if initial_balance > 0:
        account["transactions"].append(
            (datetime.now().strftime("%Y-%m-%d"), "deposit", initial_balance)
        )

    return account

def perform_transaction(account, amount, transaction_type):

    date = datetime.now().strftime("%Y-%m-%d")

    if transaction_type == "deposit":
        account["balance"] += amount
        account["transactions"].append((date, "deposit", amount))
        print(f"₦{amount:.2f} deposited successfully.")

    elif transaction_type == "withdraw":
        if amount > account["balance"]:
            print("Insufficient funds. Withdrawal denied.")
        else:
            account["balance"] -= amount
            account["transactions"].append((date, "withdraw", amount))
            print(f"₦{amount:.2f} withdrawn successfully.")

    else:
        print("Invalid transaction type.")

def show_transaction_history(account):

    print("\n=== TRANSACTION HISTORY ===")

    if len(account["transactions"]) == 0:
        print("No transactions found.")
        return

    for date, trans_type, amount in account["transactions"]:
        print(f"{date} | {trans_type.title()} | ₦{amount:.2f}")

def monthly_summary(account):

    total_deposits = 0
    total_withdrawals = 0

    for _, trans_type, amount in account["transactions"]:

        if trans_type == "deposit":
            total_deposits += amount

        elif trans_type == "withdraw":
            total_withdrawals += amount

    print("\n=== MONTHLY SUMMARY ===")
    print(f"Account Holder: {account['name']}")
    print(f"Total Deposits: ₦{total_deposits:.2f}")
    print(f"Total Withdrawals: ₦{total_withdrawals:.2f}")
    print(f"Final Balance: ₦{account['balance']:.2f}")


name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

account = create_account(name, balance)

while True:

    print("\n===== BANK MENU =====")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transaction History")
    print("4. Monthly Summary")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        perform_transaction(account, amount, "deposit")

    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))
        perform_transaction(account, amount, "withdraw")

    elif choice == "3":
        show_transaction_history(account)

    elif choice == "4":
        monthly_summary(account)

    elif choice == "5":
        print("Thank you for banking with us!")
        break

    else:
        print("Invalid choice. Try again.")



#Assignment 4


def validate_credentials(username, password):
    results = {
        "username_valid": True,
        "password_valid": True,
        "errors": []
    }

    if len(username) < 6:
        results["username_valid"] = False
        results["errors"].append("Username must be at least 6 characters long.")

    if " " in username:
        results["username_valid"] = False
        results["errors"].append("Username must not contain spaces.")

    if not username[0].isalpha():
        results["username_valid"] = False
        results["errors"].append("Username must start with a letter.")

    uppercase = 0
    lowercase = 0
    digits = 0
    special = 0

    for char in password:

        if char.isupper():
            uppercase += 1

        elif char.islower():
            lowercase += 1

        elif char.isdigit():
            digits += 1

        else:
            special += 1


    if len(password) >= 8:

        if uppercase > 0:

            if lowercase > 0:

                if digits > 0:

                    if special > 0:
                        pass

                    else:
                        results["password_valid"] = False
                        results["errors"].append(
                            "Password must contain at least one special character."
                        )

                else:
                    results["password_valid"] = False
                    results["errors"].append(
                        "Password must contain at least one digit."
                    )

            else:
                results["password_valid"] = False
                results["errors"].append(
                    "Password must contain at least one lowercase letter."
                )

        else:
            results["password_valid"] = False
            results["errors"].append(
                "Password must contain at least one uppercase letter."
            )

    else:
        results["password_valid"] = False
        results["errors"].append(
            "Password must be at least 8 characters long."
        )

    return results

def generate_suggestions(password):

    suggestions = []

    if len(password) < 8:
        suggestions.append("Increase password length to at least 8 characters.")

    if not any(char.isupper() for char in password):
        suggestions.append("Add at least one uppercase letter.")

    if not any(char.islower() for char in password):
        suggestions.append("Add at least one lowercase letter.")

    if not any(char.isdigit() for char in password):
        suggestions.append("Add at least one digit.")

    if not any(not char.isalnum() for char in password):
        suggestions.append("Add at least one special character.")

    if not suggestions:
        suggestions.append("Excellent password! No improvements needed.")

    return suggestions

test_data = [
    ("mustard", "Pass123!"),          
    ("blueboy", "Pass123!"),      
    ("chiamaka chidi", "Pass123!"),    
    ("scepter123", "password"),       
    ("tegah01", "Password1"),      
    ("Michael7", "Strong@123")   
]

for username, password in test_data:

    print("=" * 60)
    print(f"Username: {username}")
    print(f"Password: {password}")

    result = validate_credentials(username, password)

    print("\nValidation Result:")
    print(result)

    if not result["password_valid"]:
        print("\nSuggestions:")
        for tip in generate_suggestions(password):
            print("-", tip)

    print()