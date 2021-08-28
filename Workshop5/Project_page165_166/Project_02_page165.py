"""
Author: Tran Dinh Hoang
Date: 16/08/2021
Program: Project_02_page165.py
Problem:
    2.  Write a program that allows the user to navigate the lines of text in a file. The program should prompt
        the user for a filename and input the lines of text into a list. The program then enters a loop in which
        it prints the number of lines in the file and prompts the user for a line number. Actual line numbers
        range from 1 to the number of lines in the file. If the input is 0, the program quits. Otherwise, the
        program prints the line associated with that number.

* * * * * ============================================================================================= * * * * *

Solution:
    Display result
        Enter the input file name: ../fileTest/testProj2.txt
        The file has 5 lines.
        Enter a line number [0 to quit]: 2
        2 : it prints the number of lines in the file and prompts the user for a line number. Actual line numbers

        The file has 5 lines.
        Enter a line number [0 to quit]: 0

"""


# Take the input file name
inName = input("Enter the input file name: ")

# Open the input file and read the text
inputFile = open(inName, 'r')
lines = []
for line in inputFile:
    lines.append(line)


while True:
    print("The file has", len(lines), "lines.")
    if len(lines) == 0:
        break
    lineNumber = int(input("Enter a line number [0 to quit]: "))
    if lineNumber == 0:
        break
    elif lineNumber >= len(lines):
        print("ERROR: line number must be less than", len(lines))
    else:
        print(lineNumber, ":", lines[lineNumber])


