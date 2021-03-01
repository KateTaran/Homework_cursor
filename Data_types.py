int_a = 55
print (id(int_a))
tr_b = 'cursor'
print(id(tr_b))
set_c = {1, 2, 3}
print(id(set_c))
lst_d = [1, 2, 3]
print(id(lst_d))
dict_e = {'a': 1, 'b': 2, 'c': 3}
print(id(dict_e))

lst_d += set_c
print(id(lst_d))

int_a = 55
print (type(int_a))
str_b = 'cursor'
print (type(str_b))
set_c = {1, 2, 3}
print (type(set_c))
lst_d = [1, 2, 3]
print (type(lst_d))
dict_e = {'a': 1, 'b': 2, 'c': 3}
print (type(dict_e))

print(isinstance(int_a, int))
print(isinstance(str_b, str))
print(isinstance(set_c, set))
print(isinstance(lst_d, list))
print(isinstance(dict_e, dict))

