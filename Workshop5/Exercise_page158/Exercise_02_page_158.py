"""
Author: Tran Dinh Hoang
Date: 07/08/2021
Program: Exercise_02_page_158.py
Problem:

    2.  Assume that the variable data refers to the dictionary {'b':20, 'a':35}. Write the values of the
        following expressions:

        a.  data['a']
        b.  data.get('c', None)
        c.  len(data)
        d.  data.keys()
        e.  data.values()
        f.  data.pop('b')
        g.  data # After the pop above

* * * * * ============================================================================================= * * * * *

Solution:
    Display result:
        a. 35
        b. None
        c. 2
        d. dict_keys(['b', 'a'])
        e. dict_values([20, 35])
        f. 20
        g. {'a': 35}

"""

data = {'b': 20, 'a': 35}

# a
print("a. %s" % data['a'])

# b
print("b. %s" % data.get('c', None))

# c
print("c. %s" % len(data))

# d
print("d. %s" % data.keys())

# e
print("e. %s" % data.values())

# f
print("f. %s" % data.pop('b'))

# g
print("g. %s" % data)
