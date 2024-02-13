# +	Addition	x + y
# -	Subtraction	x - y
# *	Multiplication	x * y	
# /	Division	x / y
# %	Modulus	x % y
# ** Exponentiation	x ** y	
# // Floor division	x // y

# simple calculation
totalBalance = 240000
selfDep = 20000 * 2

tickets = 30000 * 2
visa_fees = 7700 * 2
rentDeposit = 32000

subTotal = tickets + visa_fees + rentDeposit
payment = totalBalance - subTotal
final = totalBalance - subTotal + selfDep

print("------------- Initial -------------")
print("Total Balance:", totalBalance)
print("------------- Payments -------------")
print("Total Withdraw:", subTotal)
print("Total Remain:", payment)
print("------------- Incoming Deeposit -------------")
print("Total Incoming:", selfDep)
print("Final Remain:", final)