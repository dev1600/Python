class Student:
    
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
        
    # Below is used to overload + operator
    def __add__(self,other):
        m1=self.m1+other.m1
        m2=self.m2+other.m2
        s3=Student(m1,m2)
        return s3
    
s1=Student(70,67)
s2=Student(80,90)
total=s1+s2
print(total.m1,total.m2)