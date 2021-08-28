"""
Author: Tran Dinh Hoang
Date: 31/07/2021
Program: Exersice_04_page_125.py
Problem:
    4.  Write a code segment that prints the names of all of the items in the current working directory.

* * * * * ============================================================================================= * * * * *

Solution:
    Display result:
        Exercise_01_page_125.py
        Exercise_02_page_125.py
        Exercise_03_page_125.py
        Exercise_04_page_125.py
        Exercise_05_page_125.py

"""
import os

for listFile in os.listdir():
    print(listFile)

