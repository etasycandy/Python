"""
Author: Trần Đình Hoàng
Date: 17/07/2021
Program: Exercise_03_page_85.py
Problem:
    3.  Write a loop that counts the number of space characters in a string. Recall that the
        space character is represented as ' '.

Solution:
    Display result:
        There are 2 space characters in the string Trần Đình Hoàng

"""

name = "Trần Đình Hoàng"
count = 0

for i in name:
    if i == ' ':
        count += 1

print("There are", count, "space characters in the string", name)
