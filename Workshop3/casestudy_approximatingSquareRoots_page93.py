"""
Author: Trần Đình Hoàng
Date: 17/07/2021
Program: casestudy_approximatingSquareRoots_page93.py
Problem:
    Compute the square root of a number.
        1.  The input is a number.
        2.  The outputs are the program's estimate of the square root using Newton's method of
            successive approximations, and Python's own estimate using math.sqrt.

Solution:
    Display result:
        Enter a positive number: 5
        The program's estimate: 2.236067977499978
        Python's estimate:  2.23606797749979

"""

# Receive the input number from the user
import math

x = float(input("Enter a positive number: "))

# Initialize the tolerance and estimate
tolerance = 0.000001
estimate = 1.0

# Perform the successive approximations
while True:
    estimate = (estimate + x / estimate) / 2
    difference = abs(x - estimate ** 2)
    if difference <= tolerance:
        break

# Output the result
print("The program's estimate:", estimate)
print("Python's estimate: ", math.sqrt(x))
