from functools import lru_cache
from timeit import default_timer as timer

@lru_cache()
def fib(n):
    if(n<=1):
        return n
    return fib(n-1)+fib(n-2)

start=timer()
print(fib(40))
end=timer()
print(end-start)