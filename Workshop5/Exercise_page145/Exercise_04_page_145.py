"""
Author: Tran Dinh Hoang
Date: 07/08/2021
Program: Exercise_04_page_145.py
Problem:

    4.  What is a mutator method? Explain why mutator methods usually return the value None.

* * * * * ============================================================================================= * * * * *

Solution:
    Display result:
        95

"""

data = [21, 12, 20, 5, 26, 11]

# print(sum(data))
total = 0
for value in data:
    total += value

print(total)

