"""
Author: Tran Dinh Hoang
Date: 30/08/2021
Program: Exercise_02_page_194.py
Problem:

    2.  What is the scope of a variable? Give an example.

* * * * * ============================================================================================= * * * * *

Solution:
    Result:
        -   A scope is a region of the program and broadly speaking there are three places, where variables can
            be declared:
            +   Inside a function or a block which is called local variables,
            +   In the definition of function parameters which is called formal parameters.
            +   Outside of all functions which is called global variables.
        -   As in the example below, the scope of variable 'n' is only invoked and used within the scope of the
            function 'example'.

"""

# Ex:

def example(n):
    if n > 0:
        print(n)
        example(n - 1)


def main():
    example(4)


if __name__ == '__main__':
    main()
