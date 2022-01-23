# Below is outer class
class Students:
    
    def __init__(self,name,rollno,brand,cpu):
        self.name = name
        self.rollno = rollno
        # Creating Laptop type variable lap in Constructor
        self.lap=self.Laptop(brand,cpu)
        
    def show(self):
        print(f'Name is {self.name} Roll no is {self.rollno}')
    
    # Below is inner class of Students
    class Laptop:
        
        def __init__(self,brand,cpu):
            self.brand=brand
            self.cpu=cpu
        
        def display(self):
            print(f"Brand is {self.brand}")
            print(f"CPU is {self.cpu}\n")
            
"""You can create object of inner class inside the outer class
                            or
    You can create object of inner class outside the outer class
    provided you use outer class name to call it"""
    
s1 = Students('Mark',24,"HP","i5")
s2 = Students("Jenny",25,"Dell","i7")

s1.lap.display()
s2.lap.display()