lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
lst_to_sort.sort()
print(lst_to_sort)

lst_to_sort.sort(reverse=True)
print(lst_to_sort)

lst_to_sort1 = list(map(lambda x: x * 2, lst_to_sort))
print(lst_to_sort1)

list_A = [2, 3, 4]
list_B = [5, 6, 7]
list_C = list(map(pow, list_A, list_B))
print(list_C)

from functools import reduce
num1 = reduce(lambda x, y: x + y, lst_to_sort)
print(num1)

lst_filer = list(filter(lambda x: (x % 2 == 1), lst_to_sort))
print(lst_filer)

b = range(-10, 10)
list_filter1 = list(filter(lambda x: x < 0, b))
print(list_filter1)

list_1 = [1,2,3,5,7,9]
list_2 = [2,3,5,6,7,8]
list_3 = list(filter(lambda x: x in list_1, list_2))
print(list_3)