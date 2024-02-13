# basic Python GUI use tkinter
import csv
from tkinter import *

# create root window
root = Tk()

# root window title and dimension
root.title("Basic Python")

lbl = Label(root, text = "Create CSV file?")
lbl.grid()

def CSV():
    with open('Sample.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        colHeader = ['fname', 'lname', 'postion']
        writer.writerow(colHeader)
        writer.writerow(['Pawit', 'Yodkaset', 'Developer',])
        writer.writerow(['Shawn', 'Michael', 'Maarketing',])
        writer.writerow(['Willis', 'Lee', 'Security',])
        writer.writerow(['Marcus', 'Lampbirge', 'Engineer',])

        try:
            res = "You've successfully created CSV file."
            lbl.configure(text = res)
            print('Success Created CSV file.')
        except:
            print("An exception occurred")

# adding Entry Field
# txt = Entry(root, width=10)
# txt.grid(column =1, row =0)

# Set Button to execute CSV function
btn = Button(
    root, 
    text = "Click", 
    fg = "black", 
    command=CSV
)

btn.grid(
    column=0, 
    row=1,
)

# Set geometry (widthxheight)
root.geometry('800x600')

# all widgets will be here
# Execute Tkinter
root.mainloop()
