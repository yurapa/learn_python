#!/usr/bin/python
# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8


################################################################################

# Практичне завдання № 2.1
# Вхідні дані: 3 дійсних числа - аргументи командного рядка.
# Вихідні дані: результат обчислення формули
# Аргументи передаються в порядку, зазначеному у формулі, назви змінних можуть 
# використовуватися будь-які.

# Приклад:
# Вхідні дані: 1 1 0.25
# Приклад виклику: python lab2_1.py 1 1 0.25
# Результат: 1.59576912161


import math
import sys

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
result = math.exp( - (a - b)**2/(2*c**2) ) / ( math.sqrt(2 * math.pi) * c )

print result