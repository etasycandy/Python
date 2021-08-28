"""
Author: Tran Dinh Hoang
Date: 07/08/2021
Program: Exercise_05_page_145.py
Problem:

    5.  Assume that data refers to a list of numbers, and result refers to an empty list. Write a loop that adds
        the nonzero values in data to the result list, keeping them in their relative positions and excluding the
        zeros.

* * * * * ============================================================================================= * * * * *

Solution:
    Display result:
        [21, 12, 20, 5, 26, 11]

"""

data = [21, 12, 20, 0, 5, 26, 11]
result = []

for value in data:
    if value != 0:
        result.append(value)

print(result)
