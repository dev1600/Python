import functools

def repeat(num):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(num):
                result=func(*args,**kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num=3)
def greet(name):
    print(f"Hello {name}")
    
greet("Dev")