"""
Author: Trần Đình Hoàng
Date: 12/07/2021
Program: project_04_page_62.py
Problem:
    4.  Write a program that takes the radius of a sphere (a floating-point number) as
        input and then outputs the sphere’s diameter, circumference, surface area, and volume.

Solution:
    Display result:
        Enter of radius: 3

        Diameter of sphere = 6.0
        Circumference of sphere = 18.85
        Surface area of sphere = 113.1
        Volume of sphere = 113.1

"""

import math

radius = float(input("Enter of radius: "))
diameter = radius * 2
circumference = math.pi * diameter
S = math.pi * pow(diameter, 2)
V = 4/3 * math.pi * pow(radius, 3)

# print display result
print("\nDiameter of sphere =", diameter)
print("Circumference of sphere =", round(circumference, 2))
print("Surface area of sphere =", round(S, 2))
print("Volume of sphere =", round(V, 2))

