"""
Author: Tran Dinh Hoang
Date: 30/08/2021
Program: Project_04_page203.py
Problem:
    4.  Restructure Newton’s method (Case Study 3.6) by decomposing it into three cooperating functions. The newton
        function can use either the recursive strategy of Project 1 or the iterative strategy of Case Study 3.6.
        The task of testing for the limit is assigned to a function named limitReached, whereas the task of computing
        a new approximation is assigned to a function named improveEstimate. Each function expects the relevant
        arguments and returns an appropriate value.

* * * * * ============================================================================================= * * * * *

Solution:
    Display result
        Enter a positive number or 'E' to exit: 123
        The program's estimate:  11.090536508377188
        Python's estimate:  11.090536506409418
        Enter a positive number or 'E' to exit: e

"""

import math

def limitReached(x, estimate):
    return abs(x - pow(estimate, 2))


def improveEstimate(x, estimate):
    return (estimate + x / estimate) / 2


def newton(x, estimate = 1.0):
    if limitReached(x, estimate) <= 0.000001:
        return estimate
    else:
        estimate = newton(x, improveEstimate(x, estimate))
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
