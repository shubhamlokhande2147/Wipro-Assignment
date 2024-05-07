class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, vehicle_cost):
        self.__vehicle_id = vehicle_id
        self.__vehicle_type = vehicle_type
        self.__vehicle_cost = vehicle_cost
        self.__premium_amount = 0

    def get_vehicle_id(self):
        return self.__vehicle_id

    def set_vehicle_id(self, vehicle_id):
        self.__vehicle_id = vehicle_id

    def get_vehicle_type(self):
        return self.__vehicle_type

    def set_vehicle_type(self, vehicle_type):
        self.__vehicle_type = vehicle_type

    def get_vehicle_cost(self):
        return self.__vehicle_cost

    def set_vehicle_cost(self, vehicle_cost):
        self.__vehicle_cost = vehicle_cost

    def get_premium_amount(self):
        return self.__premium_amount

    def calculate_premium(self):
        if self.__vehicle_type == "Two Wheeler":
            self.__premium_amount = self.__vehicle_cost * 0.02
        elif self.__vehicle_type == "Four Wheeler":
            self.__premium_amount = self.__vehicle_cost * 0.06
        else:
            print("Invalid vehicle type")

    def display_vehicle_details(self):
        print("Vehicle ID:", self.__vehicle_id)
        print("Vehicle Type:", self.__vehicle_type)
        print("Vehicle Cost:", self.__vehicle_cost)
        print("Premium Amount:", self.__premium_amount)


class TwoWheeler(Vehicle):
    def __init__(self, vehicle_id, vehicle_cost):
        super().__init__(vehicle_id, "Two Wheeler", vehicle_cost)


class FourWheeler(Vehicle):
    def __init__(self, vehicle_id, vehicle_cost):
        super().__init__(vehicle_id, "Four Wheeler", vehicle_cost)


# Test the program
two_wheeler = TwoWheeler("TW001", 50000)
two_wheeler.calculate_premium()
two_wheeler.display_vehicle_details()

four_wheeler = FourWheeler("FW001", 100000)
four_wheeler.calculate_premium()
four_wheeler.display_vehicle_details()
