"""
Author: Tran Dinh Hoang
Date: 31/07/2021
Program: Exersice_03_page_106.py
Problem:
    3.  Assume that the variable data refers to the string "myprogram.exe". Write the expressions that perform
        the following tasks:

* * * * * ============================================================================================= * * * * *

Solution:
    Display result:
        y d n a C y s a t E

"""

myString = "EtasyCandy"
length = len(myString)
for index in range(length - 1, -1, -1):
    print(myString[index], end=' ')
