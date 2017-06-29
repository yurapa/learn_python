
################################################################################
### Dictionaries
# A dictionary is similar to a list, but you access values by looking up a key instead of an index.
# A key can be any string or number. Dictionaries are enclosed in curly braces.

d = {'key1' : 1, 'key2' : 2, 'key3' : 3}
print d # {'key3': 3, 'key2': 2, 'key1': 1}

residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}
print residents['Puffin'] # 104
print residents['Sloth'] # 105
print residents["Burmese Python"] # 106


# Add element:
# dict_name[new_key] = new_value
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
menu["kampot"] = 4.5


# The length len() of a dictionary is the number of key-value pairs it has.
# Each pair counts only once, even if the value is a list.
# (That's right: you can put lists inside dictionaries!)
print len(menu)
print menu


# Items can be removed from a dictionary with the del command:
# del dict_name[key_name]
zoo_animals = {
    'Unicorn' : 'Cotton Candy House',
    'Sloth' : 'Rainforest Exhibit',
    'Bengal Tiger' : 'Jungle House',
    'Atlantic Puffin' : 'Arctic Exhibit',
    'Rockhopper Penguin' : 'Arctic Exhibit'
}
del zoo_animals['Bengal Tiger']


################################################################################
webster = {
    "Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

for key in webster:
    print webster[key]
