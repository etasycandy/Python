"""
Author: Tran Dinh Hoang
Date: 07/08/2021
Program: Exercise_04_page_149.py
Problem:

    4.  Define a function named summation. This function expects two numbers, named low and high, as arguments.
        The function computes and returns the sum of the numbers between low and high, inclusive.

* * * * * ============================================================================================= * * * * *

Solution:
    Display result:
        10

"""

def summation(low, high):
    total = 0
    for index in range(low, high + 1):
        total += index
    return total

# main
low = 1
high = 5
print(summation(low, high))

