"""
Author: Tran Dinh Hoang
Date: 07/08/2021
Program: Exercise_03_page_158.py
Problem:

    3.  Assume that the variable data refers to the dictionary {'b':20, 'a':35}. Write the expressions that
        perform the following tasks:

        a.  Replace the value at the key 'b' in data with that value is negation.
        b.  Add the key/value pair 'c':40 to data.
        c.  Remove the value at key 'b' in data, safely.
        d.  Print the keys in data in alphabetical order.

* * * * * ============================================================================================= * * * * *

Solution:
    Display result:
        a. 35
        b. None
        c. 2
        d. dict_keys(['b', 'a'])

"""

data = {'b': 20, 'a': 35}

# a
data['b'] = -20
print("a. %s" % data)

# b
b = {'c': 40}
data.update(b)
print("b. %s" % data)

# c
data.pop('b')
print("c. %s" % data)

# d
data1 = {'b': 20, 'a': 35}
a = {}
keys = list(data1)
keys.sort()
for item in keys:
    print(data1[item], end=', ')
