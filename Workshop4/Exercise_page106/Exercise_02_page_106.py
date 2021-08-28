"""
Author: Tran Dinh Hoang
Date: 31/07/2021
Program: Exersice_02_page_106.py
Problem:
    2.  Assume that the variable data refers to the string "myprogram.exe". Write the expressions that perform
        the following tasks:

        a.  Extract the substring "gram" from data
        b.  Truncate the extension ".exe" from data
        c.  Extract the character at the middle position from data

* * * * * ============================================================================================= * * * * *

Solution:
    Display result:
        gram
        myprogram
        r

"""

data = 'myprogram.exe'

print(data[5:9])
print(data[:9])
print(data[(len(data)//2)])
