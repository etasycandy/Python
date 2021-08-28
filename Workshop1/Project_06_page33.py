"""
Author: Tran Dinh Hoang
Date: 05/07/2021
Program: Project_06_page33.py
Problem:
    6.  Write and test a program that computes the area of a circle. This program should
        request a number representing a radius as input from the user. It should use the formula
        3.14 * radius ** 2 to compute the area and then output this result suitably labeled.

* * * * * ============================================================================================= * * * * *

Solution:
    --> Display: "  Enter with radius: 2
                    The area is 12.56 circular units. "
"""

radius = float(input("Enter with radius: "))
area = 3.14 * radius ** 2
print("The area is", area, "circular units.")