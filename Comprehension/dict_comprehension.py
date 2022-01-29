# dict={0:'item0',
#       1:'item1',
#       ....}
# We can do the aboe in a pythonic way

dict1={i:f'item{i}' for i in range(1000) if i%100 == 0}
print(dict1)
dict2={i:f'item{i}' for i in range(5)}
print(dict2)
# We can reverse key,value pair in python 
# using comprehension
dict2={value:key for key,value in dict2.items()}
print(dict2)