class A:
    def __init__(self):
        print('Init:A')
    def m1(self):
        print("hello m1 in A")

class B(A):
    def __init__(self):
        super().__init__()
        print("Init:B")
    def m2(self):
        print("hello B in m2")
    

b1 = B()
b1.m2()
b1.m1()
