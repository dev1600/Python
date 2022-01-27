# what enumerate does is it gives both index and item

l=['Apples','Oranges','Banana','Mangoes']
l2=enumerate(l)
print(list(l2)[0][1])

for index ,item in enumerate(l):
    print(index,item)