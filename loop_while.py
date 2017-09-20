#!/usr/bin/python
# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8


################################################################################
""" WHILE
    Більш універсальний і може працювати із будь-якою умовою:
    - коли ви очікуєте якоїсь події;
    - коли вам потрібно повторювати розрахунки до досягнення заданої точності;
    - коли ви не знаєте наперед кількість ітерацій.
"""

n = 10
i = 0
while i < 10:
    print i
    i = i + 1


n = 10
list_to_iterate = [1, 2, 3, 4, 8, 2, 43, 12, 31, 20]
i = 0
while i < len(list_to_iterate):
    print list_to_iterate[i]
    i = i + 1


sum = 0
i = 0
while sum < 100:
    i = i + 1
    sum = sum + i
