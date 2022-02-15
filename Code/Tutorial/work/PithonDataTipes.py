# Clear the terminal screen
import os
from tkinter.font import names
os.system('clear')
# os.system('sudo apt update')

###############################
# DATA TYPES
# Strings   "text", 'str'
# Numbers    (int)4 , double 2,5, float 2,2
# Lists    ["john", "Bob", "Mary"]  [0, 1, 2]
# Tuples   ("John", "Bob", "Mary") no change
# Dictionaries
# Boolean
################################

names = ["John", "Bob", "Mary"]

fav_pizza = {
    "John": "Pepperoni", 
    "Bob": "Mushroom",
    "Mary": "Cheese"
}

print (names[2])
print (fav_pizza["Mary"])