
from datetime import date

# Ordered - They maintain the order of elements.
# Mutable - Items can be changed after creation.
# Allow duplicates - They can contain duplicate value

# we call it dynamic array

friends = ['Ali', 'Omar', "Osman"]

print(friends[0])

# loop over a list
for f in friends:
    print(f)
    
# we can store different data types in list in python

things = ["agges", "table", date(2024, 9, 19), 'f']

for i in things:
    print(i)


# you can other data struture to list (dictionaries, tuples, string)

v2 = 'kim'

letters = list(v2)

print(letters) # => ['k', 'i', 'm']


# slicing list #
my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm']

print(my_list[2:])

print(my_list[:-1]) # all element expect list one


# delete from list
del my_list[1]



# delete multiple types
del my_list[1:3]

print(my_list)

# using remove function

my_list.remove('m')

# del the whole list
del my_list
