# Create a CSV file
import csv

with open('Sample.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    fieldName = ['fname', 'lname', 'postion']

    writer.writerow(fieldName)
    writer.writerow(['Pawit', 'Yodkaset', 'Developer',])
    writer.writerow(['Shawn', 'Michael', 'Maarketing',])
    writer.writerow(['Willis', 'Lee', 'Security',])
    writer.writerow(['Marcus', 'Lampbirge', 'Engineer',])

    try:
        print('Success Created CSV file.')
    except:
        print("An exception occurred")
