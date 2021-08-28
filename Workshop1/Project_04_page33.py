"""
Author: Tran Dinh Hoang
Date: 05/07/2021
Program: Project_04_page33.py
Problem:
    4.  Open an IDLE window, and enter the program from Figure 1-7 that computes
        the area of a rectangle. Load the program into the shell by pressing the F5 key,
        and correct any errors that occur. Test the program with different inputs by
        running it at least three times.

* * * * * ============================================================================================= * * * * *

Solution:
    --> Display: "  Enter with width: 10
                    Enter with height: 5
                    The area is 15 square units. "
"""

width = int(input("Enter with width: "))
height = int(input("Enter with height: "))
area = width + height
print("The area is", area, "square units.")