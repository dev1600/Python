from functools import reduce

list_i=[1,2,3,4]
num=reduce(lambda x,y:x+y,list_i)
print(num)