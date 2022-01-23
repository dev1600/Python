class Car:
    # Below variables belong to the class 
    # Shared by all instances of class
    wheels=4
    
    def __init__(self):
        # Below variables belong to instance 
        self.milage=10
        self.company="BMW"
    
c1=Car()
c2=Car()
c1.milage=20
Car.wheels=5
print(c1.wheels)
print(c2.wheels)
print("Milage is {}".format(c1.milage))