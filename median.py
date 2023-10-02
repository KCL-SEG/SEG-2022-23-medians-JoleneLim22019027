"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
import math

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = sorted([float(value) for value in input().split(",")])
        qty = len(numbers)
        if qty % 2 == 0:
            x = int(qty/2)
        else:
            x = int(math.ceil((qty/2) - 1))
        median = numbers[x]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

print(median)
