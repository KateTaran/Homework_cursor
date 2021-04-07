from math import sqrt
import logging

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
        # num_2 not input
        print(f' sqrt {num_1}  = ', sqrt(num_1))
    elif operation == "%":
        print(f'{num_1} % of {num_2} = ', num_2/100*num_1)
    else:
        break



