"""
Author: Tran Dinh Hoang
Date: 30/08/2021
Program: Exercise_02_page_199.py
Problem:

    2.  Write the code for a filtering that generates a list of the positive numbers in a list named numbers.
        You should use a lambda to create the auxiliary function.

* * * * * ============================================================================================= * * * * *

Solution:
    Result:
        [1, 2, 6]

"""

def main():
    numbers = [1, 2, -5, 6, -21]
    print(list(filter(lambda x: x > 0, numbers)))


if __name__ == '__main__':
    main()
