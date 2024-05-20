# This program is a password manager - not a very good one, because we can read all the passwords right here!

secrets = {
    "bank": "abc123",
    "insta": "passwordpassword",
    "email": "12345abcd",
    "bankadmin": "qquid93827"
}

print("All accounts:")
for key, value in secrets.items():
    print(key)

account = input("Enter an account name: ")

password = secrets[account]
print(f"The password for account {account} is {password}")
