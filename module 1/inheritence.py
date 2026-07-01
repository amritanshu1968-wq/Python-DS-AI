#define the parent class to hold general data

class Vehicle:
    #The initializer method runs automatically when an object of the class is created
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
    #a method that format and returns the vehicle details as a string
    def display_info(self):
        return f" {self.brand} ({self.year})"
    
    #define the child that automatically copy every information
class Car(Vehicle):
    pass
my_car = Car("BMW M5", 2026)

#calling the display_info method from the parent class
print(my_car.display_info())  # Output: BMW M5 (2026)

print("KOI CHUHNA NAI")

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Dog(Animal):
    def bark(self):
        return f"{self.name} is barking."

dog = Dog("Tommy", "Dog")
print(dog.bark())
