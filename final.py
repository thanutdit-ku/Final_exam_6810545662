class Person:
    def __init__(self,name):
        self.name = name
    def introduce(self):
        return f"Hi, I'm {self.name}"
    
class Customer(Person):
    def __init__(self, name):
        super().__init__(name)
        self.address = 0
    def place_order(self,item):
        self.item = item

class Driver(Person):
    def __init__(self, name, vehicle):
        super().__init__(name)
        self.vehicle = vehicle
    def deliver(self):
        print(f"{self.name} is delicering {self.item} to {self.name}")

class DeliveryOrder:
    def __init__(self,customer,item):
        self.customer = customer
        self.item = item
        self.status = "preparing"
    def assign_driver(self,driver):
        self.name = driver
    def summary(self):
        pass
customer_name1 = input("Enter your name: ")
person1 = Person(customer_name1)
customer_name2 = input("Enter your name: ")
person2 = Person(customer_name2) 
driver_name = input("Enter your name: ")
driver1 = Person(driver_name) 
print(person1.introduce())
print(person2.introduce())    
print(driver1.introduce()) 

item1 = input(f"{customer_name1} enter you items: ")     
