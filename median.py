"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
import statistics

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
        median = statistics.median(numbers)
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

print(median)
