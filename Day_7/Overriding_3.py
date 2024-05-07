class Parent:
    def purchaseBike(self):
        print("Parent wants to purchase Hero Bike")
    def marry(self):
        print("Parent decided marry for our child with ABC")
    def property(self):
        print("Car+Gold+Money")

class Child(Parent):
    def purchaseBike(self):
        print("Child wants to purchase R1-5 Bike")
    def marry(self):
        print("Child decided marry with PQR")

c = Child()
c.property()
c.purchaseBike()
