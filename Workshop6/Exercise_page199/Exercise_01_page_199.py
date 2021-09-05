"""
Author: Tran Dinh Hoang
Date: 30/08/2021
Program: Exercise_01_page_199.py
Problem:

    1.  Write the code for a mapping that generates a list of the absolute values of the numbers in a list
        named numbers.

* * * * * ============================================================================================= * * * * *

Solution:
    Result:
        [1, 2, 5, 6, 21]

"""

def main():
    numbers = [1, 2, -5, 6, -21]
    print(list(map(abs, numbers)))


if __name__ == '__main__':
    main()
