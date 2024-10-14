

country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
  "England": "London"
}

print(country_capitals)

# access dictionary values #

print(f"capital of Canada is {country_capitals['Canada']}")

# using get

best_City = country_capitals.get('England')

print(best_City)


# add dictionary value by assign a value to a new key #

country_capitals['Sudan'] = 'Khartoum'

print(f"the new capital is {country_capitals.get('Sudan')}")


## Delete from dictionary ##

## `del` key word


del country_capitals['Germany']

print(f"set after deleting: {country_capitals}")


## clear 


country_capitals.clear() # empty dictionary



print(country_capitals)
