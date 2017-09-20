#!/usr/bin/python
# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8


################################################################################
### Decision Making (РОЗГАЛУЖЕННЯ IF .. ELSE)

a = 5
b = 30


if 8 > 9:
    print "I don't printed!"
else:
    print "I get printed!"


if a > b: print "a is greater than b"


if (a > b):
    print "a is greater than b"
    print "blocks are defined by indentation"
elif (a < b):
    print "a is less than b"
else:
    print "a is equal to b"


n = int(raw_input('Input n: '))
if n > 100:
    print 'so large number!'
elif n > 10:
    print 'ok, not bad'
elif n == 0:
    print 'tricky!'
else:
    print 'hey, what are you doing?'
