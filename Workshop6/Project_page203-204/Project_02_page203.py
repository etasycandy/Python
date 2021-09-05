"""
Author: Tran Dinh Hoang
Date: 30/08/2021
Program: Project_02_page203.py
Problem:
    2.  Convert Newton’s method for approximating square roots in Project 1 to a recursive function named newton.
        (Hint: The estimate of the square root should be passed as a second argument to the function.).

* * * * * ============================================================================================= * * * * *

Solution:
    Display result
        Enter a positive number or 'E' to exit: 123
        The program's estimate:  11.090536508377188
        Python's estimate:  11.090536506409418
        Enter a positive number or 'E' to exit: e

"""

import math


def newton(x, estimate):
    # Initialize the tolerance
    tolerance = 0.000001

    # Perform the successive approximations
    if abs(x - pow(estimate, 2)) <= tolerance:
        return estimate
    else:
        estimate = newton(x, (estimate + x / estimate) / 2)
    return estimate


def main():
    # Initialize the estimate
    estimate = 1.0

    # Perform the successive approximations
    while True:
        x = input("Enter a positive number or 'E' to exit: ")
        if x.upper() == 'E':
            break
        print("The program's estimate: ", newton(float(x), estimate))
        print("Python's estimate: ", math.sqrt(float(x)))


if __name__ == "__main__":
    main()
