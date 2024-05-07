from abc import ABCMeta, abstractmethod

class DirectToHomeService:
    counter = 101
    
    def __init__(self, consumer_name):
        self.consumer_name = consumer_name
        DirectToHomeService.counter += 1
        self.consumer_number = DirectToHomeService.counter
    
    def get_consumer_number(self):
        return self.consumer_number
    
    def get_consumer_name(self):
        return self.consumer_name
    
    @abstractmethod
    def calculate_monthly_rent(self):
        pass

class BasePackage(DirectToHomeService):
    def __init__(self, consumer_name, base_pack_name, subscription_period):
        super().__init__(consumer_name)
        self.base_pack_name = base_pack_name
        self.subscription_period = subscription_period
    
    def get_base_pack_name(self):
        return self.base_pack_name
    
    def get_subscription_period(self):
        return self.subscription_period
    
    def validate_base_pack_name(self):
        valid_packs = ["Silver", "Gold", "Platinum"]
        if self.base_pack_name not in valid_packs:
            self.base_pack_name = "Silver"
            print("Base package name is incorrect, set to Silver")
    
    def calculate_monthly_rent(self):
        if 1 <= self.subscription_period <= 24:
            self.validate_base_pack_name()
            monthly_rent = {"Silver": 350.00, "Gold": 440.00, "Platinum": 560.00}
            discount_amount = 0
            if self.subscription_period > 12:
                discount_amount = monthly_rent[self.base_pack_name]
            final_rent = ((monthly_rent[self.base_pack_name] * self.subscription_period) - discount_amount) / self.subscription_period
            return final_rent
        else:
            return -1

# Testing the implementation
consumer1 = BasePackage("John", "Silver", 6)
print("Consumer Number:", consumer1.get_consumer_number())
print("Consumer Name:", consumer1.get_consumer_name())
print("Base Package:", consumer1.get_base_pack_name())
print("Subscription Period:", consumer1.get_subscription_period())
print("Monthly Rent:", consumer1.calculate_monthly_rent())

consumer2 = BasePackage("Alice", "Gold", 18)
print("\nConsumer Number:", consumer2.get_consumer_number())
print("Consumer Name:", consumer2.get_consumer_name())
print("Base Package:", consumer2.get_base_pack_name())
print("Subscription Period:", consumer2.get_subscription_period())
print("Monthly Rent:", consumer2.calculate_monthly_rent())
