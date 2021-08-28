"""
Author: Trần Đình Hoàng
Date: 12/07/2021
Program: project_09_page_63.py
Problem:
    9.  Write a program that takes as input a number of kilometers and prints the corresponding number of nautical miles.
        Use the following approximations:
        -   A kilometer represents 1/10,000 of the distance between the North Pole and the equator.
        -   There are 90 degrees, containing 60 minutes of arc each, between the North Pole and the equator.
        -   A nautical mile is 1 minute of an arc.

Solution:
    Display result:
        Enter the number of km: 123

        123.0 km = 66.42 nmi

"""
km = float(input("Enter the number of km: "))
nmi = 90 * 60 / 10000
swap = km * nmi

# print
print("\n" + str(km) + " km = " + str(swap) + " nmi")
