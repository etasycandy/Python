"""
Author: Trần Đình Hoàng
Date: 17/07/2021
Program: Exercise_02_page_70.py
Problem:
    2.  Write a loop that prints your name 100 times. Each output should begin on a new line.

Solution:
    Display result:
        Trần Đình Hoàng (1)
        ...
        Trần Đình Hoàng (100)

"""

name = "Trần Đình Hoàng"

for i in range(100):
    print(name, "(" + str(i+1) + ")")
