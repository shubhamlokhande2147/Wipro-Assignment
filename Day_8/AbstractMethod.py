from abc import ABCMeta, abstractmethod
class Parent(metaclass=ABCMeta):
    def __init__(self):
        self.num=100

    @abstractmethod
    def show(self):
        pass

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.__var=10

    def show(self):
        print(self.num)
        print(self.__var)

obj=Parent()
obj.show()
