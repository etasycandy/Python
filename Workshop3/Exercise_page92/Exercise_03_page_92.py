"""
Author: Trần Đình Hoàng
Date: 17/07/2021
Program: Exercise_03_page_92.py
Problem:
    3.  The log 2 of a given number N is given by M in the equation N 5 M2 . Using integer arithmetic,
        the value of M is approximately equal to the number of times N can be evenly divided by 2 until
        it becomes 0. Write a loop that computes this approximation of the log 2 of a given number N.
        You can check your code by importing the math.log function and evaluating the expression
        round(math.log(N, 2)) (note that the math.log function returns a floating-point value).

Solution:
    Display result:


"""
import math

N = int(input("Enter N = "))
count = 0

n = N
while n != 0:
    n = (n-1) // 2
    count += 1

print("The log 2 of a given number", N, "=", count)
print("The log 2 of a given number", N, "=", str(round(math.log2(N))))

