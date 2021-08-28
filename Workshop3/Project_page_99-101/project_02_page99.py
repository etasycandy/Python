"""
Author: Trần Đình Hoàng
Date: 17/07/2021
Program: project_02_page99.py
Problem:
    2.  Write a program that accepts the lengths of three sides of a triangle as inputs.
        The program output should indicate whether or not the triangle is a right triangle.
        Recall from the Pythagorean theorem that in a right triangle, the square of one side
        equals the sum of the squares of the other two sides.

Solution:
    Display result:
        Enter the lengths of three sides of a triangle:
        Edge A = 3
        Edge B = 4
        Edge C = 5
        Is a right triangle

"""

print("Enter the lengths of three sides of a triangle: ")
a = int(input("Edge A = "))
b = int(input("Edge B = "))
c = int(input("Edge C = "))

if a + b > c and b + c > a and a + c > b:
    if pow(a, 2) == pow(b, 2) + pow(c, 2) or pow(b, 2) == pow(a, 2) + pow(c, 2) or pow(c, 2) == pow(b, 2) + pow(a, 2):
        print("Is a right triangle")
    else:
        print("Not a right triangle")
else:
    print("Not a triangle")
