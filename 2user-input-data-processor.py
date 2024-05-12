"""
Task 1: Input Length Validator
Write a script that checks the length of the user's first name and last name. Both should be at least 2 characters long. If not, print an error message.

Task 2: Password Complexity Checker
Create a function that checks the complexity of a user's password. The password must be at least 8 characters long, contain one uppercase letter, one lowercase letter, and one number. If the password does not meet these criteria, print a message explaining the complexity requirements.

Task 3: Email Formatter
Implement a script that ensures all user email addresses are in a standard format
"""

def input_length_validator():
    while True:
        first_name = input("First name: ".capitalize())
        last_name = input("Last name: ".capitalize())
        if len(first_name) < 2 or len(last_name) < 2:
            print("Error: First name and last name must be at least 2 characters long.")
            continue
        else:
            confirm = input(f"Do you want to confirm '{str.capitalize(first_name)} {str.capitalize(last_name)}' as your first and last name? (y/n) ")
            if confirm == 'y':
                print("First name and last name are valid.")
                break
            else:
                print("Please enter your first and last name again.")

input_length_validator()

def password_complexity_checker():
    while True:
        password = input("Password: ")
        if len(password) < 8:
            print("Error: Password must be at least 8 characters long.")
            continue
        elif not any(char.islower() for char in password):
            print("Error: Password must contain at least one lowercase letter.")
            continue
        elif not any(char.isupper() for char in password):
            print("Error: Password must contain at least one uppercase letter.")
            continue
        elif not any(char.isdigit() for char in password):
            print("Error: Password must contain at least one number.")
            continue
        else:
            confirm = input("Please confirm your password: ")
            if confirm == password:
                print("Password is valid.")
                break
            else:
                print("Passwords do not match. Please enter your password again.")

password_complexity_checker()

def email_formatter(email):
    while True:
        if "@" not in email or "." not in email.split("@")[-1]:
            print("Error: Email must be in someone@example.com format.")
            continue
        else:
            confirm = input(f"Do you want to confirm '{email}' as your email? (y/n) ")
            if confirm == 'y'or "yes":
                print("Email is valid.")
                break
            else:
                print("Please enter your email again.")

email_formatter(input("Enter your email: ").strip().lower())