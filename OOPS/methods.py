
class Students:
    
    school="SFC"
    
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    def get_m1(self):
        return self.m1
    
    def get_m2(self):
        return self.m2
    
    def get_m3(self):
        return self.m3
    
    # When you want class variable use cls
    # as well as a decorator given below
    @classmethod
    def get_school(cls):
        return cls.school
    
    
s1=Students(35,40,75)
s2=Students(79,80,45) 

print("Average of student is ",Students.avg(s1))
print("Average of student is ",s2.avg())
print("School is ",Students.get_school())