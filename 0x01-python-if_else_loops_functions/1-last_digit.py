#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
num = abs(number) % 10
if number > 0:
    if num > 5:
        print("Last digit of", number, "is", num, "and is greater than 5")
    elif num == 0:
        print("Last digit of", number, "is", num, "and is 0")
    else:
        print("Last digit of", number, "is", num, "and is less than 6 and not 0")
else:
    if num > 5:
        print("Last digit of", number, "is", -num, "and is greater than 5")
    elif num == 0:
        print("Last digit of", number, "is", -num, "and is 0")
    else:
        print("Last digit of", number, "is", -num, "and is less than 6 and not 0")
