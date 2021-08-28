"""
Author: Tran Dinh Hoang
Date: 31/07/2021
Program: Exersice_05_page_125.py
Problem:
    5.  Write a code segment that prompts the user for a filename. If the file exists, the program should print
        its contents on the terminal. Otherwise, it should print an error message.

* * * * * ============================================================================================= * * * * *

Solution:
    Display result:
    
        Enter file name: Exercise_04_page_125.py
        """ """
        AUTHOR: TRAN DINH HOANG
        DATE: 31/07/2021
        PROGRAM: EXERSICE_04_PAGE_125.PY
        PROBLEM:
            4.  WRITE A CODE SEGMENT THAT PRINTS THE NAMES OF ALL OF THE ITEMS IN THE CURRENT WORKING DIRECTORY.
        
        * * * * * ============================================================================================= * * * * *
        
        SOLUTION:
            DISPLAY RESULT:
                EXERCISE_01_PAGE_125.PY
                EXERCISE_02_PAGE_125.PY
                EXERCISE_03_PAGE_125.PY
                EXERCISE_04_PAGE_125.PY
                EXERCISE_05_PAGE_125.PY
        
        """ """
        IMPORT OS
        
        FOR LISTFILE IN OS.LISTDIR():
            PRINT(LISTFILE)
        
"""

fname = input("Enter file name: ")

try:
    fh = open(fname)
except:
    print('Cannot open the file ', fname, 'please try again')
    quit()

for line in fh:
    line = line.upper()
    line = line.rstrip()
    print(line)

