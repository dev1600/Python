def dec1(funct1):
    def nowexec():
        print("Executing now")
        funct1()
        print("Executed")
    return nowexec

# Below does the same thing as done in decorator_basic.py
# we use @ 
# here the functionality of who() is extended by dec1

@dec1
def who():
    print("It's me Mario")
    
who()