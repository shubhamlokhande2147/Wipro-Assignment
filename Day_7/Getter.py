class Person:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name
       
    def get_age(self):
        return self.__age
 
p1=Person('John',20)
print(p1.get_name())
