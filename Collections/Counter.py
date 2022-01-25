from collections import Counter
a='aaaabbbbccc'

# Counter is used for counting hashable items
# Elements are stored as keys and their count as dict value

my_counter=Counter(a)
print(my_counter.keys())
print(my_counter.values())
# Returns a list with tuples 
print(my_counter.most_common(2))

#Below method is used to get all itmes in list
print(list(my_counter.elements()))
