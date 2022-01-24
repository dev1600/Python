class A:
    
    def feature1(self):
        print("Feature 1 working")
        
    def feature2(self):
        print("Feature 2 working")
 
 # Here class B inherits class A    
 # Python allows Multiple Inheritance  
class B(A):
    
    def feature3(self):
        print("Feature 3 working")
        
    def feature4(self):
        print("Feature 4 working")  
        
# Python allows Multiple Inheritance        
# class C(A,B):
#     pass

a1=A()
a1.feature1()
a1.feature2()

b1=B()
b1.feature1()
b1.feature3()