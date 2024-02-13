# Grade Calculator

A_Grade = 100
B_Grade = 70
C_Grade = 60
D_Grade = 55

grade = int(input('Enter score :'))

if grade <= A_Grade and grade >= B_Grade:
    print('You got A')
elif grade <= B_Grade and grade > C_Grade:
    print('You got B')
elif grade <= C_Grade and grade > D_Grade:
    print('You got B')
elif grade < D_Grade:
    print('You failed.')