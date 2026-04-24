#
#   1. Create a Class with instance attributes
#
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

sample = Vehicle(240, 18)
print("Vehicle max speed:", sample.max_speed, "Vehicle mileage", sample.mileage)

#
#   2. Create a Vehicle class without any variables and methods
#
class Vehicle:
    pass

#
#   3. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
#
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

bus = Vehicle("School Volvo", 180, 18)
print("Vehicle name:", bus.name, "Speed:", bus.max_speed, "Mileage:", bus.mileage)

#
#   4. Class Inheritance
#
class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers."

class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)

bus = Bus("School Volvo", 180, 18)
print(bus.seating_capacity())

#
#   5. Define a property that must have the same value for every class instance (object)
#
class Vehicle:
    color = "white"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

bus = Bus("School Volvo", 180, 18)
car = Car("Audi Q5", 240, 18)

print("Color:", bus.color, "Vehicle name:", bus.name, "Speed:", bus.max_speed, "Mileage:", bus.mileage)
print("Color:", car.color, "Vehicle name:", car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)

#
#   6. Class Inheritance
#
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100
    
class Bus(Vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10/ 100
        return amount

bus = Bus("School Volvo", 12, 50)

print("Total Bus fare is:", bus.fare())

#
#   7. Check type of an object
#
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

bus = Bus("School Volvo", 12, 50)

print(type(bus))

#
#   8. Determine if School_bus is also an instance of the Vehicle class
#
class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

bus = Bus("School Volvo", 12, 50)

print(isinstance(bus, Vehicle))

#
#   9. Check object is a subclass of a particular class
#
class Animal:
    pass

class Dog(Animal):
    pass

class Puppy(Dog):
    pass

class Cat:
    pass

print(issubclass(Dog, Animal))
print(issubclass(Animal, Dog))
print(issubclass(Cat, Animal))
print(issubclass(Puppy, Animal))

#
#   10. Calculate the area of different shapes using OOP
#
class Shape:
    def area(self):
        raise NotImplementedError("Area method must be implemented by subclasses")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

shapes = [Circle(5), Square(7), Circle(3)]

for shape in shapes:
    print(f"Area: {shape.area():.2f}")