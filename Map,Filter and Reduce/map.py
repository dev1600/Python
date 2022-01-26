# Map functions takes argument and applies the function
# to all the objects of the list/iterables
# Map returns objects

numbers=["3","34","564"]
numbers=map(lambda x:int(x)+1,numbers)
print(type(numbers))
numbers=list(numbers)
print(numbers)

def sq(a):
    return a*a
def cube(a):
    return a*a*a

num=[2,3,5,6,76,3,3,2]
square=list(map(sq,num))
print(square)

fun=[sq,cube]
for i in range(5):
    val=list(map(lambda x:x(i),fun))
    print(val)
