class Phone:
    def __init__(self, price, brand, camera):
        print("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera

    def buy(self):
        print("Buying a phone")

    def return_phone(self):
        print("Returning a phone")

class FeaturePhone(Phone):
    pass

class SmartPhone(Phone):
    def __init__(self, price, brand, camera):
        super().__init__(price, brand, camera)
        print("Inside smartphone constructor")

s = SmartPhone(20000, "Apple", 13)
s.buy()
