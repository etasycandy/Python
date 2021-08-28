"""
Author: Trần Đình Hoàng
Date: 19/07/2021
Program: project_05_page100.py
Problem:
    5.  A local biologist needs a program to predict population growth. The inputs would be the initial
        number of organisms, the rate of growth (a real number greater than 0), the number of hours it
        takes to achieve this rate, and a number of hours during which the population grows. For example,
        one might start with a population of 500 organisms, a growth rate of 2, and a growth period to
        achieve this rate of 6 hours. Assuming that none of the organisms die, this would imply that this
        population would double in size every 6 hours. Thus, after allowing 6 hours for growth, we would
        have 1000 organisms, and after 12 hours, we would have 2000 organisms. Write a program that takes
        these inputs and displays a prediction of the total population.

Solution:
    Display result:
        Enter the initial number of creatures: 1000
        Enter growth rate: 2
        Enter the time of proportional growth(h): 5
        Enter the total time of growth(h): 12
        The total population = 4800

"""

originalNumber = int(input("Enter the initial number of creatures: "))
rate = float(input("Enter growth rate: "))
time = float(input("Enter the time of proportional growth(h): "))
totalTime = float(input("Enter the total time of growth(h): "))

originalNumber *= rate
totalTime /= time

print("The total population = " + str(round(originalNumber * totalTime)))

