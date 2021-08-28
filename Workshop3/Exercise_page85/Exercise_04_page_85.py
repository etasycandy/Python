"""
Author: Trần Đình Hoàng
Date: 17/07/2021
Program: Exercise_04_page_85.py
Problem:
    4.  Assume that the variables x and y refer to strings. Write a code segment that prints
        these strings in alphabetical order. You should assume that they are not equal.

Solution:
    Display result:
        EtasyCandy
        Trần Đình Hoàng
"""

x = "Trần Đình Hoàng"
y = "EtasyCandy"

words = [x, y]
words.sort(key=lambda k: k.lower())

for word in words:
    print(word)
