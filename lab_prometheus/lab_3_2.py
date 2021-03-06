#!/usr/bin/python
# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8


################################################################################

# Практичне завдання № 3.2

# Програма має розраховувати числа послідовності Фібоначчі.
# Послідовність Фібоначчі - це послідовність чисел, в якій кожний елемент
# дорівнює сумі двох попередніх. При цьому нульовий елемент вважається
# за 0, а перший 1.
# Отже, сама послідовність виглядає наступним чином:
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, …

# Вхідні дані: ціле невід'ємне число n. (Передається в програму як аргумент командного рядка.)
# Результат роботи: значення n-го числа послідовності Фібоначчі.
# Будь ласка, не використовуйте рекурсію.

# Наприклад
# Вхідні дані: 0
# Приклад виклику: python lab3_2.py 0
# Результат: 0
# Вхідні дані: 10
# Приклад виклику: python lab3_2.py 10
# Результат: 55

import sys
a = 0
b = 1
n = int(sys.argv[1])
i = 0

for i in range(n):
    a, b = b, a + b
print a


# Another example
"""
import sys
x = int(sys.argv[1])
fib_prev = 0
fib_curr = 1
if x == 0:
    print fib_prev
else:
    if x == 1:
        print fib_curr
    else:
        for i in range(x-1):
            fib_new = fib_prev + fib_curr
            fib_prev = fib_curr
            fib_curr = fib_new
        print fib_curr
"""
