"""
Author: Trần Đình Hoàng
Date: 17/07/2021
Program: Exercise_06_page_85.py
Problem:
    6.  Construct truth tables for the following Boolean expressions:
        a.  not (A or B)
        b.  not A and not B

Solution:
    Display result:
        A    B   !A or !B    !A and !B
        1    0      False        False

"""

a = 1
b = 0

print("%4s %4s %10s %12s" % ("A", "B", "!A or !B", "!A and !B"))
print("%4s %4s %10s %12s" % (a, b, not (a or b), not a and not b))

