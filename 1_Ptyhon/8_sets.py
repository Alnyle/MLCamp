
# A set is collection of unique data => element cannot be duplicated
# imutable elements

my_set = {'friend', 'table', 1, 1}
print(my_set)


# update function  update the set with
# items other collection 
# types (lists, tuples, sets, etc

companies = {'IBM', 'Samsung'}
tech_companies = ['apple', 'google', 'apple']

companies.update(tech_companies)
print(companies)


# remove item from set

companies.discard('IBM')

print(f"set after discard: {companies}")


IDs = {1, 2, 3, 4, 5, 6}

print(sum(IDs)) # sum of the element

print(max(IDs))
