#!/usr/bin/python
# -*- coding: utf-8 -*-
# The above encoding declaration is required and the file must be saved as UTF-8

"""
Str -- рядки: 'High hopes', "The great gig in the sky", "When You're In" і т.д. 
Виглядають як текстові фрагменти будь-якої довжини - від пустого рядка і до 
нескінченності (при цьому, зверніть увагу, що консоль/термінал, у якій ми 
вводимо рядок може мати власне обмеження довжини команди і просто не дозволить 
ввести надто великий рядок за 1 раз) - взяті в одинарні чи подвійні лапки. 
Для перетворення будь-якого значення у рядок використовується функція str(): 
"""
x_int = 1
x_str = str(x_int)


################################################################################
# String Concatenation - конкатенація - додавання/склеювання рідків між собою.
# Не бажано її використовувати через засмічення памяті (не ефективного викорстання)!
print 'q' + 'w' # 'qw'
print "Life " + "of " + "Brian" # Life of Brian


################################################################################
# Explicit String Conversion
print "I have " + str(2) + " coconuts!"


################################################################################
# А ще (несподівано) рядок можна множити на ціле число X. 
# Результатом цієї операції є початковий рядок, повторений X разів.
print 'q' * 3 # 'qqq'


################################################################################
# Escaping characters
# We can use the backslash to fix the problem, like this: 
print 'There\'s a snake in my boot!'
print 'I\'ll be back.'


################################################################################
# Access by Index
c = "cats"[0] # c
n = "Ryan"[3] # n


################################################################################
# String methods
# len() - gets the length (the number of characters) of a string
# lower()
# upper()
# str()

parrot = "Norwegian Blue"

print len(parrot) # 14
print parrot.lower() # norwegian blue
print parrot.upper() # NORWEGIAN BLUE

pi = 3.14 
print str(pi) # "3.14"


################################################################################
# String Formatting with %

string_1 = "Camelot"
string_2 = "place"
print "Let's not go to %s. 'Tis a silly %s." % (string_1, string_2)


name = raw_input("What is your name?")
quest = raw_input("What is your quest?")
color = raw_input("What is your favorite color?")
print "Ah, so your name is %s, your quest is %s, " \
"and your favorite color is %s." % (name, quest, color)


################################################################################
# isalpha() returns False since the string contains non-letter characters
x = "J123"
x.isalpha()  # False


################################################################################
# .slice[1:4] - This returns everything from the letter at position 1 up till position 4.

s = "Charlie"
print s[0] # will print "C"
print s[1:4] # will print "har"


################################################################################
# http://www.astro.ufl.edu/~warner/prog/python.html

s = "Go Gators! Come on Gators!"
  x = s[3:9] #x = "Gators"
  x = s[:2] #x = "Go"
  x = s[19:] #x = "Gators!"
  x = s[-7:-2] #x = "Gator"
# int count(sub [,start[,end]]): returns the number of occurances of the substring sub in the string
  x = s.count("Gator") #x = 2
# boolean endswidth(sub [,start[,end]]): returns true if the string ends with the specified substring and false otherwise:
  x = s.endswith("Gators") #x = False
# int find(sub [,start[,end]]): returns the numeric position of the first occurance of sub in the string. Returns -1 if sub is not found.
  x = s.find("Gator") #x = 3
  x = s.find("gator") #x = -1
# string join(array): combines elements of the string array into a single string and returns it. The separator between elements is the string providing this method.
  a = ['abc','def','ghi']
  t = "--"
  x = t.join(a) #x = abc--def--ghi
# int len(string): returns the length of the string
  x = len(s) #x = 26
# string lower(): returns a version of a string with all lower case lettters.
  print s.lower() #go gators! come on gators!
# string replace(old, new [,count]): returns a copy of the string with all occurances of old replaced by new. If the optional count argument is given, only the first count occurances are replaced.
  x = s.replace("Gators","Tigers",1) #x = Go Tigers! Come on Gators!
# int rfind(sub [,start[,end]]): same as find but returns the numeric position of the last occurance of sub in the string.
  x = s.rfind("Gator") #x = 19
# array split([sep [,maxsplit]]): splits a single string into a string array using the separator defined. If no separator is defined, whitespace is used. Consecutive whitespace delimiters are then treated as one delimiter. Optionally you can specify the maximum number of splits so that the max size of the array would be maxsplit+1.
  a = s.split() #a=['Go', 'Gators!', 'Come', 'on', 'Gators!']
# boolean startswidth(sub [,start[,end]]): returns true if the string starts with the specified substring and false otherwise:
  x = s.startswith("Go") #x = True
# string strip([chars]): returns a copy of the string with leading and trailing characters removed. If chars (a string) is not specified, leading and trailing whitespace is removed.
# string upper(): returns a version of a string with all upper case lettters.
