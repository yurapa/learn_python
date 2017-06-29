
################################################################################
### LISTS
# List indices begin with 0, not 1!

zoo_animals = ["pangolin", "cassowary", "sloth", "dog"];

if len(zoo_animals) > 3:
    print "The first animal at the zoo is the " + zoo_animals[0]
    print "The second animal at the zoo is the " + zoo_animals[1]
    print "The third animal at the zoo is the " + zoo_animals[2]
    print "The fourth animal at the zoo is the " + zoo_animals[3]

print zoo_animals[2] # Access by Index


################################################################################
# Append
# append() takes exactly one argument!

letters = ['a', 'b', 'c']
letters.append('d')
print len(letters)
print letters


################################################################################
# List Slicing
# "Slicing" did not modify the original list!

letters = ['a', 'b', 'c', 'd', 'e']
slice = letters[1:3]
print slice # ['b', 'c']
print letters # ['a', 'b', 'c', 'd', 'e']


################################################################################
'''
You can slice a string exactly like a list! 
In fact, you can think of strings as lists of characters: 
each character is a sequential item in the list, starting from index 0.
'''
animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6] # The fourth through sixth characters
frog = animals[6:] # From the seventh character to the end


################################################################################
# search for an item in a list

animals = ["ant", "bat", "cat"]
print animals.index("bat")


################################################################################
# We can also insert items into a list.

animals = ["ant", "bat", "cat"]
animals.insert(1, "dog") # We insert "dog" at index 1, which moves everything down by 1.
print animals # ["ant", "dog", "bat", "cat"]


################################################################################
# Remove item from a List

print "\nRemove item from list:"
beatles = ["john","paul","george","ringo","stuart"]
beatles.remove("stuart")
print beatles # ["john","paul","george","ringo"]


################################################################################
# sort()

print "\nSorting animals:"
animals = ["cat", "ant", "bat"]
animals.sort() # Note that .sort() modifies the list rather than returning a new list.
print animals


################################################################################
### FOR .. IN ..     with List.
# If you want to do something with every item in the list, you can use a for loop.
# Example: for item in list_name:

print "\nFor .. in loop for List:"
my_list = [1,9,3,8,5,7]

for number in my_list:
    print number * 2
# 2
# 18
# 6
# 16
# 10
# 14


# a for-loop that iterates over start_list and .append()s each number squared (x ** 2) to square_list.
# Then sort square_list
print "\nSorted square of each item original list: "
start_list = [5, 3, 1, 2, 4]
square_list = []

for item in start_list:
    square_list.append(item ** 2)

square_list.sort()
print square_list
