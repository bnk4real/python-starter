import os
import sys

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_path)

from functions import functions

# Workshop 1 : Create a function called "NewFunc" and return a string
input_str = 'Pawit'
result = functions.NewFunc(input_str)
print(result)

# Project structures
# project_folder/
# └── something/
#     └── functions.py
# └── workshop1/
#     └── workshop1.py