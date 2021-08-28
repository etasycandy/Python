"""
Author: Trần Đình Hoàng
Date: 17/07/2021
Program: Exercise_02_page_92.py
Problem:
    2.  The factorial of an integer N is the product of the integers between 1 and N, inclusive.
        Write a while loop that computes the factorial of a given integer N.

Solution:
    Display result:
        Factorial of 5 = 120

"""

N = 5
gt = 1
count = N

while (0 < count <= 5):
    gt *= count
    count -= 1

print("Factorial of", N, "=", gt)
