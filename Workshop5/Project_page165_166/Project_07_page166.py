"""
Author: Tran Dinh Hoang
Date: 16/08/2021
Program: Project_07_page166.py
Problem:
    7.  Write a program that inputs a text file. The program should print the unique words in the file in
        alphabetical order.

* * * * * ============================================================================================= * * * * *

Solution:
    Display result
        Enter the input file name: ../fileTest/testProj7.txt
        After
        Define
        Employ
        Explain
        Use
        a
        able
        and
        are
        assign
        be
        chapter,
        code
        completing
        design
        effectively
        exploit
        filtering,
        for
        function
        functions
        higher-order
        in
        it
        mapping,
        namespace
        of
        optional
        parameters
        program
        recursive
        reducing
        required
        structuring
        tasks
        the
        this
        to
        top-down
        use
        useful
        why
        will
        with
        you

"""


inName = input("Enter the input file name: ")

inputFile = open(inName, 'r')
uniqueWords = []

for line in inputFile:
    words = line.split()
    for word in words:
        if not word in uniqueWords:
            uniqueWords.append(word)

uniqueWords.sort()

for word in uniqueWords:
    print(word)

