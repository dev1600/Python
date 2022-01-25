from itertools import accumulate
import operator
a=[1,2,3,4]
# 2nd arg of accumulate is a function pointer
# which can perform any operation we want 
acc=accumulate(a,func=operator.mul)
print(a)
print(list(acc))