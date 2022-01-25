from timeit import default_timer as timer

my_string= 'How,are,you,doing'

# .split() takes the delimeter as argument

my_list=my_string.split(",")
print(my_list)

#  .join method joins the strinngs again 
# here ' ' is used as delimeter but we can specify anything

new_string=' '.join(my_list)
print(new_string)

my_list=['a']*1000000

# Below is a bad method as string in python are immutable
# hence whenever we use str= str+ s we create another copy
# of str and perform operation hence it is very expensive 

start=timer()
my_string=''
for i in my_list:
    my_string=my_string+i
stop= timer()
print(stop-start)

# Below is good method of perforoming concat

start=timer()
my_string=''.join(my_list)
stop=timer()
print(stop-start)