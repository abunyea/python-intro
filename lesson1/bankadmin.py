print("~ BANK SOFTWARE 2.0 ~")
print("copyright 1987 Bank Software Enterprises LTD")
print("")
print("Welcome to Bank Software 2.0")
print("")

balance = 200

password = input("Please enter your password: ")

if password == "abc123":
    print(f"Your balance is ${balance}.")
elif password == "qquid93827":
    print("**** SECURE ****")
    print("**** Logged in as BANK ADMIN ****")
    print("You're in")
    print(f"Current balance is ${balance}.")
    balance = int(input("New balance: "))
    print(f"Your balance is now ${balance}.")
else:
    print("Unknown password, goodbye.")
