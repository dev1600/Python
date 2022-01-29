import functools

def end_decorator(func):
    # Following is called a wrapper function
    # .wraps preserves the information of func
    # Logically the code will work fine without it
    
    # We use *args and **kwargs so that we take 
    # all the parameters passed by the func
    
    @functools.wraps(func)
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