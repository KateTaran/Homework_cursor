from math import sqrt
import logging
import time
import random

#1.
log_template = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(level=logging.INFO, filename='test.log', filemode='w', format=log_template)
while True:
    lst = ['+', '-', '*', '/', '**', 'sqrt', '%']
    operation = input('''
Please choose the math operation:
+ for addition
- for subtraction
* for multiplication
/ for division
** for exponentiation
sqrt for square root
% for percentage of the number

''')

    logging.info(f'Choosed operation {operation}')
    if operation not in lst:
        print(f'Wrong operation')
        continue

    number_1 = input('Enter your first number: ')
    try:
        num_1 = float(number_1)
    except ValueError:
        print('First number is not decimal')
        continue
    logging.info(f'Choosed first number {num_1}')
    number_2 = input('Enter your second number: ')
    try:
        num_2 = float(number_2)
    except ValueError:
        print('Second number is not decimal')
        continue
    logging.info(f'Choosed second number {num_2}')

    if operation == "+":
        print(f'{num_1} + {num_2} = ', num_1 + num_2)
    elif operation == "-":
        print(f'{num_1} - {num_2} = ', num_1 - num_2)
    elif operation == "*":
        print(f'{num_1} * {num_2} = ', num_1 * num_2)
    elif operation == "/":
        try:
            num_3 = num_1 / num_2
            print(f'{num_1} / {num_2} = ', num_1 / num_2)
        except ZeroDivisionError:
            print(f'Choose another second number')
            logging.error('Divide by zero')
    elif operation == "**":
        print(f'{num_1} ** {num_2} = ', num_1 ** num_2)
    elif operation == "sqrt":
        print(f' sqrt {num_1}  = ', sqrt(num_1))
    elif operation == "%":
        print(f'{num_1} % of {num_2} = ', num_2/100*num_1)
    else:
        break


# 2.
class LowBattery(Exception):
    pass


class EmptyBattery(Exception):
    pass


class NoWater(Exception):
    pass


class OverflowGarbageCan(Exception):
    pass


class Robot_cleaner:
    battery_discharge = 5
    def __init__(self, battery_charge, filling_garbage_can, amount_of_water):
        self.battery_charge = battery_charge
        self.filling_garbage_can = filling_garbage_can
        self.amount_of_water = amount_of_water

    def move(self):
        while True:
            time.sleep(1)
            try:
                print(f'Robot cleaner moves, battery level: {self.battery_charge}')
                self.battery_charge -= self.battery_discharge
                if self.battery_charge <= 20:
                    if self.battery_charge == 0:
                        raise EmptyBattery
                    raise LowBattery
            except LowBattery:
                print(f'Warning! Battery level: {self.battery_charge}')
            except EmptyBattery:
                print(f'Battery is discharged')
                break

    def wash(self):
        if self.amount_of_water <= 0:
            raise NoWater
        else:
            print('Washing')
            self.amount_of_water = max(self.amount_of_water - random.randint(1, 10), 0)
            print(f"Water level: {self.amount_of_water}")


    def vacuum_cleaner(self):
        if self.filling_garbage_can >= 100:
            print(f"Garbage level: {self.filling_garbage_can}")
            raise OverflowGarbageCan
        else:
            print('Vacuum cleaning')
            print(f"Garbage level: {self.filling_garbage_can}")
            self.filling_garbage_can = min(self.filling_garbage_can + random.randint(10, 22), 100)

robot = Robot_cleaner(100, 0, 100)
robot.move()
robot.wash()
            


