class A:
    
    def __init__(self):
        print("In A init")
    
    def feature_A(self):
        print("Feature of A")
        
class B:
    
    # The compiler first check if there is constructor of 
    # sub class and executes it else if not present then 
    # it checks for constructor of parent class and exectures it
    
    def __init__(self):
        # super() is used to refer the super class
        # super().__init__ is used to call constructor 
        # of super class
        
        # super().__init__
        print("Init of B")
        
    def feature_B(self):
        print("Feature of B")

# In case of multiple inheritance it follows MRO for methods
# and constructors 
# Accoring to it method is executed first of the base class
# then it execution order is from Left to Right 
# In our case it will execute first constructor of A 
class C(A,B):
    
    def __init__(self):
        super().__init__()
        print("In C init")
    
    def feat(self):
        super().feature_B()
        
c1=C()
c1.feat()