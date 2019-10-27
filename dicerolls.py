# Roll a dice of any given size
# Input if you would like to roll again

import random

yes = {"yes", "y", "ys", ""}
no = {"no", "n", "nn"}

rolls = True

sides = int(input("Please tell me how many sides your dice has: "))

# while keep rolling
while rolls == True:
    print(random.randint(1, sides))
    userinput = input("Would you like to roll again?")
    if userinput in no:
        rolls = False
# /END while

print("Goodbye!")
