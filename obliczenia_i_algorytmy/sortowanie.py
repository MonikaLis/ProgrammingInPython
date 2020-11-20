import random
import math 
import numpy as np

numbers = []
numbers_test = []

for number in range(50):
    numbers.append(random.randint(1,100))

numbers_test = numbers

swapped = True
while swapped:
    swapped = False
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
            swapped = True

sorted(numbers_test)

for number in numbers:
    print("own algorithm: {}".format(number))

for number in numbers_test:
    print("built-in algorithm: {}".format(number))
