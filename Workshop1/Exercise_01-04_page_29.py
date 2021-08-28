"""
Author: Tran Dinh Hoang
Date: 05/07/2021
Program: Exersice_01-04_page_29.py
Problem:
    1.  Describe what happens when the programmer enters the string "Greetings!" in
        the Python shell.

    2.  Write a line of code that prompts the user for his or her name and saves the user’s
        input in a variable called name.

    3.  Answer the question, What is a Python script?

    4.  Explain what goes on behind the scenes when your computer runs a Python program.


* * * * * ============================================================================================= * * * * *

Solution:

    1.  Python shell error message:
        File "<input>", line 1
            Greetings!
                     ^
        SyntaxError: invalid syntax

    2.  name = str(input("Enter your name: "))

    3.  It's a language that Python already knows,
        so when certain words are input into Python like "int" Python already knows the significance of "int".

    4.  When a Python program is executed, it is translated into byte code.
        This byte code is then sent to the Python virtual machine (PVM) for further interpretation and execution.
        ....

"""
