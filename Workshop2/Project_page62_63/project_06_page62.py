"""
Author: Trần Đình Hoàng
Date: 12/07/2021
Program: project_06_page_62.py
Problem:
    6.  The kinetic energy of a moving object is given by the formula KE = (1/2)mv^2
        where m is the object’s mass and v is its velocity. Modify the program you created
        in Project 5 so that it prints the object’s kinetic energy as well as its momentum.

Solution:
    Display result:
        Enter of mass(kg): 3.535
        Enter of velocity(m/s): 5

        Object’s momentum = 17.68 (kgm/s)
        The kinetic energy = 44.19 (Jun)

"""
mass = float(input("Enter of mass(kg): "))
V = float(input("Enter of velocity(m/s): "))
M = mass * V
KE = (1/2) * mass * pow(V, 2)

print("\nObject’s momentum = " + str(round(M, 2)) + " (kgm/s)")
print("The kinetic energy = " + str(round(KE, 2)) + " (Jun)")