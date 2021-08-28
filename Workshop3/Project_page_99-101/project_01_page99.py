"""
Author: Trần Đình Hoàng
Date: 17/07/2021
Program: project_01_page99.py
Problem:
    1.  Write a program that accepts the lengths of three sides of a triangle as inputs.
        The program output should indicate whether or not the triangle is an equilateral triangle.

Solution:
    Display result:
        Enter the lengths of three sides of a triangle:
        Edge A = 2
        Edge B = 2
        Edge C = 2
        Is an equilateral triangle

"""

print("Enter the lengths of three sides of a triangle: ")
a = int(input("Edge A = "))
b = int(input("Edge B = "))
c = int(input("Edge C = "))

if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print("Is an equilateral triangle")
    else:
        print("Not an equilateral triangle")
else:
    print("Not a triangle")
