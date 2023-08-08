#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = str(number)
if number < 0:
    last_digit = int(str1[-1]) * (-1)
else:
    last_digit = int(str1[-1])
if last_digit > 5:
    str2 = "and is greater than 5"
elif last_digit == 0:
    str2 = "and is 0"
elif last_digit < 6 and last_digit != 0:
    str2 = "and is less than 6 and not 0"
print("Last digit of", number, "is", last_digit, str2)
