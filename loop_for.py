#!/usr/bin/python
# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8


################################################################################
### FOR, FOR .. IN ..

for j in range(10):
    print "Value number " + str(j)

x = 0
for j in range(10,0,-2):
    x = x + j
    print x

k = 0
for j in range(0,10):
    while(k < j):
        print "j = " + str(j) + " k = "+str(k)
        if (j == 1): break
        k = k + 1
    print "j equals k or j equals 1"

a = ["abc","def","ghi"]
for x in a:
    print x


# вивід кожного символу рядка послідовно
for letter in 'qwertyuiopasdfghjkl':
    print letter


# Можна й зациклити for цикл, якщо дуже захотіти
l = [0]
for i in l:
    l.append(i + 1)
