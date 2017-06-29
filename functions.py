#!/usr/bin/python
# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8


################################################################################
### FUNCTIONS
'''
Якщо в програмі є власні функції, вони оголошуються саме на початку - після
оголошення змінних або навіть перед ним.

raw_input(msg) або input(msg) - виводить текстовий рядок-запрошення і чекає,
поки користувач введе якісь дані і натисне Enter
'''

# text_prompt - забезпечує виконання raw_input або input незалежно від версії встановленого інтерпретатора.
def text_prompt(msg):
    try:
        return raw_input(msg)
    except NameError:
        return input(msg)


################################################################################
# Приймаємо у функцію список (масив) аргументів *args
def biggest_number(*args):
    print max(args)
    return max(args)

biggest_number(-10, -5, 5, 10)


################################################################################
def distance_from_zero(number):
    if (type(number) == int or type(number) == float):
        print abs(number)
        return abs(number)
    else:
        return "Nope"

distance_from_zero(-101)
