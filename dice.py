import random

sides = int(input("Please tell me how many sides your dice has: "))

roll = int(input("Please enter an how many times you would like to roll your dice: "))

for i in range(roll):
    print(random.randint(1, sides))