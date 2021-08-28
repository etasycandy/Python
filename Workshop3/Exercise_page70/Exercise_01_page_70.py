"""
Author: Trần Đình Hoàng
Date: 17/07/2021
Program: Exercise_01_page_70.py
Problem:
    1.  Write the outputs of the following loops:
        a.  for count in range(5):
                print(count + 1, end = " ")
        b.  for count in range(1, 4):
                print(count, end = " ")
        c.  for count in range(1, 6, 2):
                print(count, end = " ")
        d.  for count in range(6, 1, –1):
            print(count, end = " ")

Solution:
    Display result:
        a.  1 2 3 4 5
        b.  1 2 3
        c.  1 3 5
        d.  6 5 4 3 2

"""
# 1
for count in range(5):
    print(count + 1, end=" ")
# 2
print()
for count in range(1, 4):
    print(count, end=" ")
# 3
print()
for count in range(1, 6, 2):
    print(count, end=" ")
# 4
print()
for count in range(6, 1, -1):
    print(count, end=" ")
