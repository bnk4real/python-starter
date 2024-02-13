# basic if-else statement
a = 23
b = 32

if a < b:
    print("It's correct")

# Elif
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

# short hand if-else 
if a > b: print("a is greater than b")

# More than one conditions and/or/not
# For instance :
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")