# It makes a list such that the function
# return true for the given condition
list_i=range(9)

def is_greater(num):
    return num > 5

# Below statement will give elements that are >5 in above
# list
grt=list(filter(is_greater,list_i))
print(grt)