points2D=[(1,2),(5,1),(5,-1),(10,4)]

# sorted according to y value 
points2D_sorted=sorted(points2D,key=lambda x: x[1])
print(points2D)
print(points2D_sorted)

a=[1,2,3,4,5]
b=map(lambda x:x*2,a)
print(list(b))

b=filter(lambda x: x%2 ==0,a)
print(list(b))