"""
Author: Tran Dinh Hoang
Date: 30/08/2021
Program: Exercise_02_page_182.py
Problem:

    2.  The factorial of a positive integer n, fact(n), is defined recursively as follows:
                                    fact( ) n 1 5 , when n 1
                                    fact( ) n n 5 2 * fact n( ) 1 , otherwise
        Define a recursive function fact that returns the factorial of a given positive integer.

* * * * * ============================================================================================= * * * * *

Solution:
    Result:

"""

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


num = int(input("Enter the number to calculate the factorial: "))
print("Factorial of", num, "is:", fact(num))




