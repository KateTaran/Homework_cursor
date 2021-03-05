#1. Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

#2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class and will have seating_capacity own method
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity

#3. Determine which class a given Bus object belongs to (Check type of an object)
vehicle_1 = Bus(290, 75123, 45)
print(type(vehicle_1))
print(isinstance(vehicle_1, Bus))
print(issubclass(Bus, Vehicle))

#4. Determine if School_bus is also an instance of the Vehicle class
print(isinstance(vehicle_1, Vehicle))

#5. Create a new class School with get_school_id and number_of_students instance attributes
class School:
    def __init__(self, school_id, number_of_students):
        self.school_id = school_id
        self.number_of_students = number_of_students

    def get_school_id(self):
        return self.school_id

#6*. Create a new class SchoolBus that will inherit all of the methods from School and Bus and will have its own - bus_school_color
class SchoolBus(School, Bus):
    def __init__(self, school_id, number_of_students, max_speed, mileage, seating_capacity, bus_school_color):
        School.__init__(self, school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, seating_capacity)
        self.bus_school_color = bus_school_color

#7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances, one of Bear and one of Wolf,
#make a tuple of it and by using for call their action using the same method.
class Bear:
    def make_sound(self):
        print('Rrrr')

class Wolf:
    def make_sound(self):
        print('Auf')

bear = Bear()
wolf = Wolf()
for animal in (bear, wolf):
    animal.make_sound()

#8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
#otherwise return message: "Your city is too small".
class City:
    def __init__(self, name, population):
        self.name = name

    def __new__(cls, name, population):
        instance = super(City, cls).__new__(cls)
        if population > 1500:
            return instance
        else:
            print ("Your city is too small.")

#9. Override a printable string representation of the City class and return: The population of the city {name} is {population}
def __str__(self):
 return(f'The population of the city {self.name} is {self.population}')

#10*. Override magic method __add__() to perform the additional action as 'multiply' (*) the value which is greater than 10. And perform this add (+) of two instances.
class Mult:
    def __init__(self, count):
        self.count = count

    def __add__(self, other):
        if self.count > 10 and other.count > 10:
            total_count = self.count * other.count
        else:
            total_count = self.count + other.count
        return Mult(total_count)

    def __str__(self):
        return f'{self.count}'


c1 = Mult(27)
c2 = Mult(14)
c3 = c1 + c2
print(c3)

#11. The __call__ method enables Python programmers to write classes where the instances behave like functions and can be called like a function.
#Create a new class with __call__ method and define this call to return sum.
class Sum:
    def __call__(self, a, b):
        c = a + b
        return c
k = Sum()
print(k(4, 7))

#2*. Making Your Objects Truthy or Falsey Using __bool__(). Create class MyOrder with cart and customer instance attributes.
#Override the __bool__magic method considered to be truthy if the length of the cart list is non-zero. e.g.:
class MyOrder():
    def __init__(self, card, customer):
        self.card = card
        self.customer = customer

    def __bool__(self):
        if len(self.card) > 0:
            return True
        else:
            return False

order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')
print(bool(order_1))
print(bool(order_2))