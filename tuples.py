# Python Tuples are known to be unchangable varieble in the list
thistuple = ("apple", "banana", "cherry")

print(len(thistuple)) # count tuples

thistuple[1] = "mango" # this will not change the varieble

print(thistuple[1]) # This will get -> TypeError: 'tuple' object does not support item assignment