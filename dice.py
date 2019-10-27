import random

foo = input("Please enter an integer: ")

int_foo = int(foo)
#print(int_foo)
#type(int_foo)

for i in range(int_foo):
    print(random.randint(1, 6))