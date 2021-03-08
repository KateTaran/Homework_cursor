print("Anna has {} apples and {} peaches.".format(3, 5))

print("Anna has {1} apples and {0} peaches.".format(3, 5))

print("Anna has {apples} apples and {peaches} peaches.".format(apples=3, peaches=5))

print("Anna has {0:.5} apples and {1:.3} peaches.".format(3333333, 55555))

apples = "5"
peaches = "3"
print(f"Anna has {apples} apples and {peaches} peaches.")

print("Anna has %s apples and %s peaches." % (apples, peaches))

dict_fruits = {'x': apples, 'y': peaches}
print("Anna has %(x)s apples and %(y)s peaches." % dict_fruits)
