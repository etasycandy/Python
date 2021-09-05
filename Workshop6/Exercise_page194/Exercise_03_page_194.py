"""
Author: Tran Dinh Hoang
Date: 30/08/2021
Program: Exercise_03_page_194.py
Problem:

    3.  What is the lifetime of a variable? Give an example.

* * * * * ============================================================================================= * * * * *

Solution:
    Result:
        -   Lifetime defines how long the variable would be valid, i.e. Would be existent and can be used safely.
            For ex all variables defined inside a function have a lifetime that spans within the body of that
            function, and then exist from the time the function starts to execute and till the function finishes
            it execution. These variables are allocated memory on stack, the stack unwinds on return from a function
            and hence these variables are destroyed at that time.
        -   As in the example below, existence time of variable 'n' is the time from start to finish of function
            'example'

"""

def example(n):
    if n > 0:
        print(n)
        example(n - 1)


def main():
    example(4)


if __name__ == '__main__':
    main()
