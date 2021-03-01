def foo(x, y):
    if x < y:
        return x
    else:
        return y
print(foo(3, 2))

foo1 = lambda x, y: x if x < y else y
print(foo1(3, 2))

foo2 = lambda x, y, z: z if y < x and x > z else y
print(foo2(1, 2, 3))

def foo3(x, y, z):
    if y < x and x > z:
        return z
    else:
        return y
print(foo3(1, 2, 3))