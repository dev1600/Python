class Computer:
    # Below is python constructor
    def __init__(self,cpu,ram):
        print("__init__() is invoked")
        self.cpu=cpu
        self.ram=ram
        
    # self means that the object of class type is a prammeter
    def config(self):
        print(f"CPU is {self.cpu}\nRAM is {self.ram}")
        
com1=Computer("Ryzen5 3600H",'16 GB')
com2=Computer('i5 9600k','32 GB')
# print(type(com1))
# Below are ways to call the above function
Computer.config(com1)
com2.config()