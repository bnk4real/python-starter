# Calculate number

def Plus():
    num1 = int(input("Enter First Number :"))
    num2 = int(input("Enter Second Number :"))
    operator = input("Enter Operator :")
    if operator == "+":
        x = num1 + num2
        print(x)    
    cont = input("Continue? :")
    while cont == "yes":
        Plus()
    else:
        return

print('Welcome to Cal+')
start = input("What you want to do? ")
if start == "plus":
    Plus()