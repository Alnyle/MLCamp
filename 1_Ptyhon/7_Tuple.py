
# Ordered - They maintain the order of elements.
#Immutable - They cannot be changed after creation.
#Allow duplicates - They can contain duplicate values.#

lang = ('English', 'Spanish', 'Korean')

# lang[0] = 'Greek'

# can not delete tuple but can delete from it's self

del lang

def addElement(my_tuple, ele):
    appended_tuple = my_tuple + (ele,)
    print(appended_tuple)
    
addElement((5, 6, 5), 22)