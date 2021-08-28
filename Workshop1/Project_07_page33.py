"""
Author: Tran Dinh Hoang
Date: 05/07/2021
Program: Project_07_page33.py
Problem:
    7.  Write and test a program that accepts the user’s name (as text) and age (as a number)
        as input. The program should output a sentence containing the user’s name and age.

* * * * * ============================================================================================= * * * * *

Solution:
    --> Display: "  Name: Trần Đình Hoàng
                    Age: 12
                    Your name is Trần Đình Hoàng and you are 12 year(s) old. "
"""

name = str(input("Name: "))
age = int(input("Age: "))

print("Your name is", name, "and you are", age, "year(s) old.")