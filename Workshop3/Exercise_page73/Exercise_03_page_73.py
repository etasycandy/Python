"""
Author: Trần Đình Hoàng
Date: 17/07/2021
Program: Exercise_03_page_73.py
Problem:
    3.  Write a format operation that builds a string for the float variable amount that has
        exactly two digits of precision and a field width of zero.

Solution:
    Display result:
        3.14

"""
import math

amount = math.pi

print(f"{amount:0.2f}")
# or
# print("%0.2f" % amount)
