from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Dict, Any
import random
import uuid
import time


class Animal(ABC):

    def __init__(self, power: int, speed: int):
        self.id = uuid.uuid4()
        if power < 25 or power > 100 or speed < 25 or speed > 100:
            raise Exception("wrong power or speed")
        self.max_power = power
        self.current_power = power
        self.speed = speed

    @abstractmethod
    def eat(self, forest: Forest):
        raise NotImplementedError

class Predator(Animal):

    def eat(self, forest: Forest):
        prey = random.choice(list(forest.animals.values()))

        if prey.id == self.id:
            print(f'Predator was unlucky and he was without dinner.')
        else:
            print(f'Predator hunts for prey.')
            if self.speed > prey.speed:
                print(f'Predator caught up prey.')
                if self.current_power > prey.current_power:
                    current_power = self.max_power * 0.5 + self.current_power
                    if current_power < self.max_power:
                        self.current_power = current_power
                        print(f'The animal regains power')
                    else:
                        self.current_power = self.max_power
                    forest.remove_animal(prey)
                    print(f'Predator eats prey.')
                else:
                    cur_power = self.current_power - self.max_power*0.3
                    self.current_power = cur_power
                    curr_power = prey.current_power - prey.max_power * 0.3
                    prey.current_power = curr_power
                    print(f'Predator and prey lost power.')
                    if prey.current_power < 25:
                        forest.remove_animal(prey)
                    if self.current_power < 25:
                        forest.remove_animal(self)
            else:
                print(f'Predator lost prey')

class Herbivorous(Animal):

    def eat(self, forest: Forest):
        current_power = self.max_power*0.5 + self.current_power
        if current_power < self.max_power:
            self.current_power = current_power
            print(f'The animal regains power')
        else:
            self.current_power = self.max_power


class Forest:

    def __init__(self):
        self.animals: Dict[str, Animal] = dict()

    def add_animal(self, animal: Animal):
        print('New animal is', animal)
        self.animals.update({animal.id: animal})

    def remove_animal(self, animal: Animal):
        print(animal, 'is dying')
        self.animals.pop(animal.id)

    def is_predator_exist(self):
        for i in list(self.animals.values()):
            if isinstance(i, Predator):
                return True
        return False






def animal_generator():
    while True:
        yield random.choice([Herbivorous(random.randint(25, 100), random.randint(25, 100)), \
                                   Predator(random.randint(25, 100), random.randint(25, 100))])




dark_forest = Forest()
# print(dark_forest.__dict__)

# rabbit = Herbivorous(25, 42)
# for i in range(10):
#     dark_forest.add_animal(Herbivorous(25, 42))


# squirrel = Herbivorous(random.randint(25, 100), random.randint(25, 100))
# print(squirrel)

for k in range(20):
    dark_forest.add_animal(next(animal_generator()))

print(f'There are {dark_forest.animals} in the forest.')


while dark_forest.is_predator_exist():
    animal_keys = list(dark_forest.animals.keys())
    for i in animal_keys:
        if i in dark_forest.animals:
            dark_forest.animals[i].eat(dark_forest)