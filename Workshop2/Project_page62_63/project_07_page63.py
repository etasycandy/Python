"""
Author: Trần Đình Hoàng
Date: 12/07/2021
Program: project_07_page_63.py
Problem:
    7.  Write a program that calculates and prints the number of minutes in a year.

Solution:
    Display result:
        Enter of year: 2021

        The number of minutes in 2021 is : 525600 minutes.

"""
def checkYear(year):
    return (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0))

year = int(input("Enter of year: "))

if checkYear(year):
    day = 366
else:
    day = 365

minutesOfYear = day * 24 * 60

print("\nThe number of minutes in " + str(year) + " is : " + str(minutesOfYear) + " minutes.")
