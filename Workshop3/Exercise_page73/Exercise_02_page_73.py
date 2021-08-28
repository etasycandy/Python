"""
Author: Trần Đình Hoàng
Date: 17/07/2021
Program: Exercise_02_page_73.py
Problem:
    2.  Write a code segment that displays the values of the integers x, y, and z on a single
        line, such that each value is right-justified with a field width of 6.

Solution:
    Display result:
           123    234    432

"""
x = 123
y = 234
z = 432

print("%6s %6s %6s" % (x, y, z))
