"""
Task 1: Command Parser
Write a script that takes a user's text input and identifies if it contains one of the predefined commands (e.g., "help", "issue", "contact support"). If a command is found, print a response related to the command.

Task 2: Issue Categorizer
If the user's input contains the word "issue", further categorize the issue based on keywords such as "login", "performance", "error", etc. Print out the category of the issue for the support team.
"""
def find_predefined_commands():
    user_input1 = input("How can I help you with?: ")
    predefined_commands = {
        "help": "Sure thing here is the help information I have on that",
        "issue": "Thank you for reporting this issue to us!",
        "contact support": "Here is the number for our support team 1-888-888-8888."
    }
    for key, value in predefined_commands.items():
        if user_input1.find(key) != -1:
            print(value)
        break

find_predefined_commands()

def command_parser():
    predefined_commands = {
        'B': "You are being redirected to our billing department.",
        "C": "This is our Complaints or Suggestions department!",
        "S": "Here is the number for our support team 1-888-888-8888."
    }

    while True:
        user_input = input("Hello there! Here are some topics that we can provide you assistance with: 'Billing' (B), 'Complaints or Suggestions' (C), 'Contact Support' (S). Exit (E): ").strip().upper()

        if user_input == 'E':
            print("Thank you for your time.")
            break
        
        if user_input in predefined_commands:
            if user_input == "B":
                print(predefined_commands["B"])
            elif user_input == "C":
                print(predefined_commands["C"])
                cs_dept = input("Would you like to file a complaint (C) or leave a suggestion (S)?: ").strip().upper()
                if cs_dept == "C":
                    print("We value you as our customer and we are really sorry that you are not 100% satisfied.")
                    print(input("Tell us what is bothering you: "))
                    print("Thank you for your time.")
                elif cs_dept == "S":
                    print("We would love to know what suggestions you have.")
                    print(input("Tell us what you would like to suggest: "))
                    print("Thank you for your time.")
            elif user_input == "S":
                print(predefined_commands["S"])
        else:
            print("Invalid input. Please try again.")

command_parser()