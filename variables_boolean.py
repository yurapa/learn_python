#!/usr/bin/python
# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8


################################################################################
### BOOLEAN

# not is evaluated first;
# and is evaluated next;
# or is evaluated last.

True or False
(3 < 4) and (5 >= 5)
this() and not that()


False or not True and True = False
False and not True or True = True
True and not (False or False) = True
not not True or False and not True = True
False or not (True and True) = False


################################################################################
### ПЕРЕТВОРЕННЯ ТИПІВ ДАНИХ

int(True) == 1
int(False) == 0
float(True) == 1.0
float(False) == 0.0
str(True) == ‘True’
str(False) == ‘False’

bool(None) == False
bool(0) == False
bool(0.0) == False
bool('') == False

bool(1) == True
bool(10) == True
bool(-1.1) == True
bool('False') == True
bool(-100500) == True
