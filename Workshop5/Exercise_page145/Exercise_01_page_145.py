"""
Author: Tran Dinh Hoang
Date: 07/08/2021
Program: Exercise_01_page_145.py
Problem:
    1.  Assume that the variable data refers to the list [5, 3, 7]. Write the values of the following expressions:

        a.  data[2]
        b.  data[-1]
        c.  len(data)
        d.  data[0:2]
        e.  0 in data
        f.  data + [2, 10, 5]
        g.  tuple(data)

* * * * * ============================================================================================= * * * * *

Solution:
    Display result:
        a.  7
        b.  7
        c.  3
        d.  [5, 3]
        e.  False
        f.  [5, 3, 7, 2, 10, 5]
        g.  (5, 3, 7)

"""

data = [5, 3, 7]

print("a. ", data[2])
print("b. ", data[-1])
print("c. ", len(data))
print("d. ", data[0:2])
print("e. ", 0 in data)
print("f. ", data + [2, 10, 5])
print("g. ", tuple(data))

