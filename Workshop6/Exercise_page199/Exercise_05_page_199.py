"""
Author: Tran Dinh Hoang
Date: 30/08/2021
Program: Exercise_05_page_199.py
Problem:

    5.  Three versions of the summation function have been presented in this chapter. One uses a loop, one uses
        recursion, and one uses the reduce function. Discuss the costs and benefits of each version, in terms of
        programmer time and computational resources required.

* * * * * ============================================================================================= * * * * *

Solution:
    Result:
        I'm a King

"""
from builtins import range
from functools import reduce
import timeit


# Loop
def summationLoop(lower, upper):
    """Returns the sum of the numbers from lower through upper."""
    sum = 0
    for i in range(lower, upper + 1):
        sum += i
    return sum


# recursion
def summationRecursion(lower, upper):
   """Returns the sum of the numbers from lower through upper."""
   if lower > upper:
       return 0
   else:
       return lower + summationRecursion(lower + 1, upper)


# reduce function
def summationReduce(lower, upper):
    """Returns the sum of the numbers from lower through upper."""
    if lower > upper:
        return 0
    else:
        return reduce(lambda x, y: x + y, range(lower, upper + 1))


def main():
    loop_time = timeit.timeit('Exercise_05_page_199.summationLoop(1, 100)', setup="import Exercise_05_page_199", number=10000)
    recursion_time = timeit.timeit('Exercise_05_page_199.summationRecursion(1, 100)', setup="import Exercise_05_page_199", number=10000)
    reduce_time = timeit.timeit('Exercise_05_page_199.summationReduce(1, 100)', setup="import Exercise_05_page_199", number=10000)
    print(f"loop_time: {loop_time}sec - number_optimize: {round(loop_time/loop_time)}(times)")
    print(f"recursion_time: {recursion_time}sec - number_optimize: {round(loop_time/recursion_time)}(times)")
    print(f"reduce_time: {reduce_time}sec - number_optimize: {round(loop_time/reduce_time)}(times)")


if __name__ == '__main__':
    main()
