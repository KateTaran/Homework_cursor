#1. Make the class with composition.
class Laptop:
    def __init__(self):
        self.battery = Battery(10000)

class Battery:
    def __init__(self, capacity):
        self.capacity = capacity

laptop = Laptop()

#2. Make the class with aggregation.
class Guitar:
    def __init__(self, guitarstring):
        self.guitarstring = guitarstring

class GuitarString:
    def __init__(self):
        pass

guitarstring = GuitarString()
guitar = Guitar(guitarstring)

#3. Make class with one method "add_nums" with 3 parameters, which returns sum of these parameters.
#Note: this method should not take instance as first parameter.

class Calc:

    @staticmethod
    def add_nums(a, b, c):
       return a + b + c

calc = Calc()
print(Calc.add_nums(1, 2, 3))

#4.
"""
    Make class which takes 1 parameter on init - list of ingredients and defines instance attribute ingredients.
    It should have 2 methods:
    carbonara (['forcemeat', 'tomatoes']) and bolognaise (['bacon', 'parmesan', 'eggs'])
    which should create Pasta instances with predefined list of ingredients.
    Example:
        pasta_1 = Pasta(["tomato", "cucumber"])
        pasta_1.ingredients will equal to ["tomato", "cucumber"]
        pasta_2 = Pasta.bolognaise()
        pasta_2.ingredients will equal to ['bacon', 'parmesan', 'eggs']
    """
class Pasta:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbonara(cls):
        return Pasta(['forcemeat', 'tomatoes'])

    @classmethod
    def bolognaise(cls):
        return Pasta(['bacon', 'parmesan', 'eggs'])

pasta_1 = Pasta(['forcemeat', 'tomatoes'])
pasta_2 = Pasta.bolognaise()
pasta_3 = Pasta(['bacon', 'parmesan', 'eggs'])
pasta_4 = Pasta.carbonara()
print(pasta_1.ingredients)
print(pasta_2.ingredients)
print(pasta_3.ingredients)
print(pasta_4.ingredients)

#5.
"""
    Make class, which has max_visitors_num attribute and its instances will have visitors_count attribute.
    In case of setting visitors_count - max_visitors_num should be checked,
    if visitors_count value is bigger than max_visitors_num - visitors_count should be assigned with max_visitors_num.
    Example:
        Concert.max_visitor_num = 50
        concert = Concert()
        concert.visitors_count = 1000
        print(concert.visitors_count)  # 50
    """
class Concert:
    max_visitors_num = 0

    def __init__(self,  visitors_count=0):
        self.visitors_count = visitors_count

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, visitors):
        if visitors > self.max_visitors_num:
            self._visitors_count = self.max_visitors_num
        else:
            self._visitors_count = visitors

Concert.max_visitors_num = 50
concert = Concert(1000)
#concert.visitors_count = 38
print(concert.visitors_count)

#6.
"""
   Create dataclass with 7 fields - key (int), name (str), phone_number (str), address (str), email (str), birthday (str), age (int)
   """
import dataclasses
@dataclasses.dataclass()

class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    email: str
    birthday: str
    age: int

#7.
""" Create the same class (6) but using NamedTuple """

import collections

AddressBookDataClass = collections.namedtuple('AddressBookDataClass',['key', 'name', 'phone_number', 'email', 'birthday', 'age'])

#8.
"""
    Create regular class taking 7 params on init - key, name, phone_number, address, email, birthday, age
    Make its str() representation the same as for AddressBookDataClass defined above.
    """
class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return (f'AddressBook(key={self.key}, name={self.name}, phone_number={self.phone_number},address={self.address},'\
               f' email={self.email}, birthday={self.birthday}, age={self.age})')

#9.
"""
    Change the value of the age property of the person object
    """
class Person:
    name = "John"
    age = 36
    country = "USA"

person = Person()
#Person.age = 54
setattr(person, "age", 54)
print(person.age)

#10.
"""
    Add an 'email' attribute of the object student and set its value
    Assign the new attribute to 'student_email' variable and print it by using getattr
    """

class Student:
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name

kate = Student(43, 'Kate')

setattr(kate, 'student_email', 'student43@gmail.com')
print(getattr(kate, 'student_email'))

#11.
"""
   By using @property convert the celsius to fahrenheit
   Hint: (temperature * 1.8) + 32)
   """
class Celsius:

    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def conv(self):
        return ((self._temperature * 1.8) + 32)

celsius = Celsius(10)
print(f'{celsius.conv}')
