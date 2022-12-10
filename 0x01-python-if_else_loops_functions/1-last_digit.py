#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
pos_statement = "Last digit of {} is {} and is greater than."
zero_statement = "Last digit of {} is {} and is 0."
else_statement = "Last digit of {} is {} and is less than 6 and not 0."
if last_digit > 5:
    print(pos_statement.format(number, last_digit))
elif last_digit == 0:
    print(zero_statement.format(number, last_digit))
elif (last_digit < 6) and (last_digit != 0):
    print(else_statement.format(number, last_digit))
