"""
Author: Tran Dinh Hoang
Date: 31/07/2021
Program: Exersice_04_page_106.py
Problem:
    4.  Assume that the variable myString refers to a string, and the variable reversedString refers to an empty
        string. Write a loop that adds the characters from myString to reversedString in reverse order.

* * * * * ============================================================================================= * * * * *

Solution:
    Display result:
        y d n a C y s a t E

"""

myString = 'EtasyCandy'
reversedString = ''

length = len(myString)
for index in range(length - 1, -1, -1):
    reversedString += myString[index] + ' '

print(reversedString)

