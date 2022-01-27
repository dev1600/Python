from concurrent.futures import Executor


# A decorator takes in a function adds some functionality
# and returns it.It is part of metaprogramming

def function1():
    print("Hello World")

# Creates a copy of function1
func2=function1
# del keyword can delete any object
del function1
func2()

def execute(func):
    func('this is from print function')
    
def dec1(func1):
    def nowexec():
        print("\nExecuting now")
        func1()
        print("Executed")
    return nowexec

def who():
    print("It's me mario")

f=dec1(who)
print(f())