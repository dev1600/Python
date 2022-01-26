from logging import exception


x=-5
# if x < 0:
#     raise Exception('x should be positive')

# We can also give assertion given below
# will give assert error

# assert(x>=0) 

# try:
#     a=5/0
# except Exception as e:
#     print("Dividing it zero")
#     print(e)
    
try:
    a=5/0
    b=x+1
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)
else:
    print("Everythin is fine")
finally:
    print("Finally clause will always run ")
    
print('Out of exception')