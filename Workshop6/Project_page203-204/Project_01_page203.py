"""
Author: Tran Dinh Hoang
Date: 30/08/2021
Program: Project_01_page203.py
Problem:
    1.  Package Newton’s method for approximating square roots (Case Study 3.6) in a function named newton.
        This function expects the input number as an argument and returns the estimate of its square root.
        The script should also include a main function that allows the user to compute square roots of inputs
        until she presses the enter/return key.

* * * * * ============================================================================================= * * * * *

Solution:
    Display result
        Enter a positive number or 'E' to exit: 21
        The program's estimate:  4.582575694960138
        Python's estimate:  4.58257569495584
        Enter a positive number or 'E' to exit: 12
        The program's estimate:  3.4641016533502986
        Python's estimate:  3.4641016151377544
        Enter a positive number or 'E' to exit: e

"""
import math


def newton(x):
    # Initialize the tolerance and estimate
    tolerance = 0.000001
    estimate = 1.0

    # Perform the successive approximations
    while True:
        estimate = (estimate + x / estimate) / 2
        difference = abs(x - pow(estimate, 2))
        if difference <= tolerance:
            break
    return estimate


def main():
    # Perform the successive approximations
    while True:
        x = input("Enter a positive number or 'E' to exit: ")
        if x.upper() == 'E':
            break
        print("The program's estimate: ", newton(float(x)))
        print("Python's estimate: ", math.sqrt(float(x)))


if __name__ == "__main__":
    main()

