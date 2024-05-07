from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):
    @abstractmethod
    def area(self):
        pass
 
class Rectangle(Shape):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth
 
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
   
 
s1 = Rectangle(10, 20)
res = s1.area()
print('Rectangle Area= ', res)

s2 = Square(10)
res = s2.area()
print('Square Area= ', res)
