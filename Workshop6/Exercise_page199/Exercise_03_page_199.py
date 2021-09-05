"""
Author: Tran Dinh Hoang
Date: 30/08/2021
Program: Exercise_03_page_199.py
Problem:

    3.  Write the code for a reducing that creates a single string from a list of strings named words.

* * * * * ============================================================================================= * * * * *

Solution:
    Result:
        I'm a King

"""

from functools import reduce


def main():
    words = ["I'm", "a", "King"]
    print(reduce(lambda x, y: x + " " + y, words))


if __name__ == '__main__':
    main()
