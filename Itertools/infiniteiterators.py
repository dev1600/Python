from itertools import count,cycle,repeat

for i in count(10):
    print(i)
    if(i==15):
        break
    
a=[1,2,3,4]
count=0
for i in cycle(a):
    if(count>3):
        break
    print(a)
    count=count+1
    
for i in repeat(2,4):
        print(i)
