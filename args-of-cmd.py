#!/usr/bin/python
# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8


################################################################################
### аргументами командного рядка

""" Вони розділяються між собою пробілами. А, якщо в якості параметра нам
    необхідно передати рядок з кількох слів, він береться у лапки.

    Щоб прочитати ці параметри з нашої програми, необхідно підключити модуль
    (ще одну бібліотеку функцій) sys. Він містить багато всього,
    але нас буде цікавити лише його змінна sys.argv,
    в якій зберігаються аргументи командного рядка, з якими запущено програму.

    Під номером (індексом) 0 знаходиться ім’я запущеного файлу.
    Під номером 1 -- перше значення, під номером 2 -- друге та ін.
"""

import sys

x = int(sys.argv[1])
y = int(sys.argv[2])
print x + y
print sys.argv # print list of arguments


# example 1
sum = 0
for arg in sys.argv[1:]: # перебрати всі аргументи, виключивши нульовий
    sum = sum + int(arg) # не забути конвертувати в число для додавання
print sum


# example 2
# Або визначити кількість переданих аргументів та вивести повідомлення
# про помилку у разі їх нестачі:
if len(sys.argv) != 4:
    print 'triangle should have 3 sides, please input 3 numbers'
else:
    print 'OK'
