class Computer:
    
    def __init__(self):
        self.name='Devansh'
        self.age=21
    
    # elf is kind of a ptr works same as ->
    # when we use self it means that all updation 
    # have to be done on the object from which the method 
    # is invoked   
    def update(self):
        self.age=22
        
    # Comparing objects
    def compare(self,other):
        if(self.age == other.age):
            return True
        else:
            return False
        
c1=Computer()
c2=Computer()
# Below prints the address of memory
print(id(c1))
c1.update()

if(c1.compare(c2) == False):
    print("Age is not equal")
else:
    print("Age is equal")

