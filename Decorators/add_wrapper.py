def end_decorator(func):
    
    def wrapper(*args,**kwargs):
        print('Start of decorator')
        result=func(*args,*kwargs)
        print('End of decorator')
        return result
    return wrapper

@end_decorator
def add(x):
    return x+5

res=add(5)
print(res)