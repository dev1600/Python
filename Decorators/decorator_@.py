def dec1(funct1):
    def nowexec():
        print("Executing now")
        funct1()
        print("Executed")
    return nowexec

@dec1
def who():
    print("It's me Mario")
    
who()