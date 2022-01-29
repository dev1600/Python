from abc import ABC,abstractmethod

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass
    
class Rectangle(Shape):
    
    def __init__(self):
        self.length=6
        self.width=7
        
    def area(self):
        return self.length*self.width

rect=Rectangle()
print(rect.area())