"""
Author: Trần Đình Hoàng
Date: 19/07/2021
Program: project_09_page101.py
Problem:
    9.  Write a program that receives a series of numbers from the user and allows the user to press the enter key
        to indicate that he or she is finished providing inputs. After the user presses the enter key, the program
        should print the sum of the numbers and their average.

Solution:
    Display result:
        Enter a string of numbers: 123456789
        Total of string =  45
        Average of string =  5.0

"""

num = int(input("Enter a string of numbers: "))
total = 0
count = 0

for i in str(num):
    total += int(i)
    count += 1

average = total / count
print("Total of string = ", total, "\nAverage of string = ", round(average, 2))
