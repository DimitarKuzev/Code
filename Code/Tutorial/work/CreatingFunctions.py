from logging import logMultiprocessing
import os
from turtle import clear
from unicodedata import name
from xml.dom.pulldom import START_ELEMENT
os.system('clear')

#########################
# Функция в Python 

print("Hello World!")
# това всъщност е функция. function(arguments)
# Ето как да създадеш своя функция:

def  mathit(num1, num2):
#    print(num1 + num2)
     return (num1 + num2)
    

#def nameit(first_name, name, last_name, x):
 #   ifelse
 #   looping 
 #   variables 
 #   print('Hello' + first_name + name + last_name + x)

# nameit(" john")
# nameit()    error - give a 1 parameter - function have 1 param.
# nameit(name)   # same thinks  - expect 4 parameters.
# by order 
# nameit("Mitko", 'Dimitar', 'Kuzev', "40")
# mathit(9, 1)
# print(mathit(9, 1))

outcome = mathit(9, 1)

print(outcome * 20)


