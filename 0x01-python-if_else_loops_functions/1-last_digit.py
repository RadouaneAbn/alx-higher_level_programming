#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    L_num = -(abs(number) % 10)
else:
    L_num = abs(number) % 10

print("Last digit of", number, "is", L_num, end=' ')

if L_num == 0:
    print("and is 0")
elif L_num > 5:
    print("and is greater than 5")
elif L_num < 6:
    print("and is less than 6 and not 0")
