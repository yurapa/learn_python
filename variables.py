
# type() function returns the type of the data it receives as an argument

print type(42) # <type 'int'>
print type(4.2) # <type 'float'>
print type('spam') # <type 'str'>
print type(('spam',)) # <type 'tuple'>

ar1 = {} # <type 'dict'>
ar2 = [] # <type 'list'>
ar3 = () # <type 'tuple'>

print type(ar1) # <type 'dict'>
print type(ar2) # <type 'list'>
print type(ar3) # <type 'tuple'>
