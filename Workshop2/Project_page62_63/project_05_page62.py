"""
Author: Trần Đình Hoàng
Date: 12/07/2021
Program: project_05_page_62.py
Problem:
    5.  An object’s momentum is its mass multiplied by its velocity. Write a program
        that accepts an object’s mass (in kilograms) and velocity (in meters per second) as
        inputs and then outputs its momentum.

Solution:
    Display result:
        Enter of mass(kg): 3.335
        Enter of velocity(m/s): 5

        Object’s momentum = 16.68 (kgm/s)

"""
mass = float(input("Enter of mass(kg): "))
V = float(input("Enter of velocity(m/s): "))
M = mass * V
print("\nObject’s momentum = " + str(round(M, 2)) + " (kgm/s)")
