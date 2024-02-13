# user input

username = input("Enter username:")
password = input("Enter password:")
print("Username is: " + username)

# Masked password the first 3 chars and the last 3 chars
maskedPass = password[3:5]
xxx = maskedPass.replace(password[3:5], "xxx")

print("Password is: " + xxx + maskedPass + xxx)