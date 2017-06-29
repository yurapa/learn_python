#!/usr/bin/python
# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8


#+---+---+---+---+---+---+
#| P | Y | T | H | O | N |
#+---+---+---+---+---+---+


################################################################################
### COMMENTS

# short comment

"""
Here the program begins. This piece of text will be ignored while executing the program
"""


################################################################################
# просто вивести результат на екран, наприклад, командою print.
# Ви можете зустріти різні варіанти запису print - з дужками та без. 
# У python 2.7 обидва є вірними і ви можете використовувати їх в своєму коді:
print 'Hello!'
print('My name is Boris.')


################################################################################
### АРИФМЕТИЧНІ ДІЇ (вбудовані в ядро - Built-In Functions):

# додавання (+)
# віднімання (-)
# множення (*)
# ділення (/)
# піднесення у степінь (**)
# ділення націло (//)
# взяття остачі (%) від ділення націло

print (2+2)**2 % 10 # 6
print (2+2)**2 % 10.0 # 6.0
print 10/3 # 3
print 3/2 * 1.0 # 1.0
print 3.0/2 * 1 # 1.5


################################################################################
### МАТЕМАТИЧНІ ФУНКЦІЇ (вбудовані в ядро - Built-In Functions)

# abs(x) - absolute value (модуль від числа). Приймає тільке одне значення. Повертає завжди тільки додатнє число.
    print abs(-42) # 42
# bin(x) - переведення числа у двійкову систему числення
# hex(x) - переведення числа у шістнадцяткову систему числення
# max(x,y) - пошук максимуму серед чисел, може приймати будь-яку кількість аргументів
    print max(1, 2, 3) # 3
# min(x,y) - пошук мінімуму серед чисел, може приймати будь-яку кількість аргументів
    print min(1, 2, 3) # 1
# round(x) - округлення числа
# round(x,y) - округлення числа x із вказаною точністю - y знаків після коми
print bin(64) # 0b1000000
