#1. словник елементами якого буде пара ключ:значення де ключ - мітка часу, значення - репліка в даний момент часу
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

#2. файл в якому знаходиться текст з якого видалені всі мітки часу. всі субтитри повинні мати вигляд простого тексту.
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



