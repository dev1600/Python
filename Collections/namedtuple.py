from collections import namedtuple

# namedtuple is similar to struct
# Here a class is created with name
# Point and and x and y as its variable
# just like a strcut in C/C++

Point=namedtuple('Point','x,y')
pt=Point(1,"hello")
new_pt=Point(1,1.4455)
print(pt.x,pt.y)
print(new_pt.x+new_pt.y)