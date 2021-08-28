"""
Author: Trần Đình Hoàng
Date: 12/07/2021
Program: project_08_page_63.py
Problem:
    8.  Light travels at 3 * 10^8 meters per second. A light-year is the distance a light beam
        travels in one year. Write a program that calculates and displays the value of a
        light-year.


Solution:
    Display result:
        The value of a light-year = 9467280000000000 mét

"""

year = 365.25
vLight = 3 * pow(10, 8)
swapMinutes = year * 24 * 60 * 60
SLight = vLight * swapMinutes

# print
print("\nThe value of a light-year = " + str(round(SLight)) + " mét")

