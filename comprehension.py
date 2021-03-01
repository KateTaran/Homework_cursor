lst = []
for num in range(10):
    if num % 2 == 1:
        lst.append(num ** 2)
    else:
        lst.append(num ** 4)
print(lst)

list_comp = [num ** 2 if num % 2 == 1 else num ** 4 for num in range(10)]
print(list_comp)

list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
print(list_comprehension)

list_1 = []
for num in range(10):
    if num % 2 == 0:
        list_1.append(num // 2)
    else:
        list_1.append(num * 10)
print(list_1)

d = {}
for num in range(1, 11):
    if num % 2 == 1:
        d[num] = num ** 2
print(d)

d_1 = {num: num ** 2 for num in range(1, 11) if num % 2 == 1}
print(d_1)

d2 = {}
for num in range(1, 11):
    if num % 2 == 1:
        d2[num] = num ** 2
    else:
        d2[num] = num // 0.5
print(d2)

d_3 = {num: num ** 2 if num % 2 == 1 else num // 0.5 for num in range(1, 11)}
print(d_3)

dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
print(dict_comprehension)

dict_1 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_1[x] = x ** 3
print(dict_1)

dict_comprehension1 = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
print(dict_comprehension1)

dict_2 = {}
for x in range(10):
    if x ** 3 % 4 == 0:
        dict_2[x] = x ** 3
    else:
        dict_2[x] = x
print(dict_2)