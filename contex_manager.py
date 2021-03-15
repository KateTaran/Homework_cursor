import pickle
import openpyxl

#1.1 словник елементами якого буде пара ключ:значення де ключ - мітка часу, значення - репліка в даний момент часу
dict_from_text = {}
lst = []
file = open("task1.txt", "r")
lst = file.readlines()

count = 0
for el in lst:
    count += 1
    if count % 2 == 1:
        #print (f"{count} {el} {lst[count]}")
        content = lst[count].replace("\n", "")
        key_1 = el.replace("\n", "")
        dict_from_text[key_1] = content
print(dict_from_text)

#1.2 файл в якому знаходиться текст з якого видалені всі мітки часу. всі субтитри повинні мати вигляд простого тексту.
lst_1 = []
file = open("task1.txt", "r")
lst_1 = file.readlines()
#print(lst)
lst_2 = [el.replace("\n", "") for el in lst_1]
#print(lst_1)

for el in lst_2:
    if len(el) < 6:
        lst_2.remove(el)
#print(lst_1)
my_string = "".join(lst_2)
print(my_string)
# for el in lst_2:
#     if len(el) > 5:
#         print (el)

#2. в файлі task2 збережений список, відкрийте цей файл, прочитайте вміст, і знайдіть середнє арифметичне чисел що знаходяться в списку
file = open("task2", "rb")
lst_3 = pickle.load(file)
print(lst_3)
s_a = sum(lst_3)/len(lst_3)
print(s_a)

#3. Використовуючи openpyxl (або будь-яку іншу зручну для вас бібліотеку), напишіть контекстний менеджер для роботи з ексель.
#Даний менеджер повинен бути аналогом методу open()
class OpenEx:
    def __init__(self, file_name):
        self.file_obj = openpyxl.load_workbook(file_name)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file_obj.close()


with OpenEx('task3.xlsx') as file:
    sheet = file.active
    sheet['A1'] = 100
    print(sheet['A1'].value)
    file.save('task3.xlsx')