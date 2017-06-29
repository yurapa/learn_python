#!/usr/bin/python
# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8


################################################################################
# Будь який файл (.py) - це вже модуль.
# Порядок імпортування модулів: системні, чиїсь, свої.

# import module = generic import
import math
print math.sqrt(25)


# from module import function = function import
from math import sqrt
print sqrt(36)


# Universal Imports = to import everything from the module
from module import * # bad style!!!
