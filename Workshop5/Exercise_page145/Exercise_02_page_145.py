"""
Author: Tran Dinh Hoang
Date: 07/08/2021
Program: Exercise_02_page_145.py
Problem:

    2.  Assume that the variable data refers to the list [5, 3, 7]. Write the expressions that perform the
        following tasks:

        a.  Replace the value at position 0 in data with that value is negation.
        b.  Add the value 10 to the end of data.
        c.  Insert the value 22 at position 2 in data.
        d.  Remove the value at position 1 in data.
        e.  Add the values in the list newData to the end of data.
        f.  Locate the index of the value 7 in data, safely.
        g.  Sort the values in data.

* * * * * ============================================================================================= * * * * *

Solution:
    Display result:
        a.  [-5, 3, 7]
        b.  [-5, 3, 7, 10]
        c.  [-5, 3, 22, 10]
        d.  [-5, 22, 10]
        e.  [-5, 22, 10, 21, 12, 20, 5, 3]
        f.  3
        g.  [-5, 3, 5, 10, 12, 20, 21, 22]

"""

data = [5, 3, 7]

# a
data[0] = -5
print("a. ", data)

# b
data.append(10)
print("b. ", data)

# c
data[2] = 22
print("c. ", data)

# d
data.pop(1)
print("d. ", data)

# e
newData = [21, 12, 20, 5, 3]
for i in newData:
    data.append(i)
print("e. ", data)

# f
print("f. ", data[7])

# g
data.sort()
print("g. ", data)



