"""
Author: Trần Đình Hoàng
Date: 17/07/2021
Program: Exercise_05_page_70.py
Problem:
    5.  Assume that the variable teststring refers to a string. Write a loop that prints
        each character in this string, followed by its ASCII value.

Solution:
    Display result:
        E = 69; t = 116; a = 97; s = 115; y = 121; C = 67; a = 97; n = 110; d = 100; y = 121;

"""

name = "EtasyCandy"

for i in name:
    print(i, "=", ord(i), end="; ")
