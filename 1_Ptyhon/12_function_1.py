

def display_info(first, second):
    print(f"{first} {second}")
    


display_info(second = "Mohammud", first = "Yassiar")
display_info("Ali", 'Omsan')


# Python Function With Arbitrary Arguments #

# allow us to pass a varying number of values during a function call.

def get_sum(*numbers):
    s = 0
    
    for i in numbers:
        s += i
    return s

res = get_sum(1, 2, 3)

print(res)