"""
Author: Tran Dinh Hoang
Date: 30/08/2021
Program: Exercise_04_page_199.py
Problem:

    4.  Modify the summation function presented in Section 6.2 so that it includes default arguments for a step
        value and a function. The step value is used to move to the next value in the range. The function is
        applied to each number visited, and the function’s returned value is added to the running total. The
        default step value is 1, and the default function is lambda that returns its argument (essentially an
        identity function). An example call of this function is summation(l, 100, 2, math.sqrt), which returns
        the sum of the square roots of every other number between 1 and 100. The function can also be called as
        usual, with just the bounds of the range.

* * * * * ============================================================================================= * * * * *

Solution:
    Result:
        Sum = 13.625201915741993

"""
import math
from functools import reduce


def summation(lower, upper, step, functionArg):
    """Returns the sum of the numbers from lower through upper."""
    if lower > upper:
        return 0
    else:
        return reduce(lambda x, y: functionArg(x) + functionArg(y), range(lower, upper + 1, step))


def main():
    print("Sum =", summation(1, 100, 2, math.sqrt))


if __name__ == '__main__':
    main()