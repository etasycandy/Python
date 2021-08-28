"""
Author: Tran Dinh Hoang
Date: 16/08/2021
Program: Project_08_page166.py
Problem:
    8.  A file concordance tracks the unique words in a file and their frequencies. Write a program that
        displays a concordance for a file. The program should output the unique words and their frequencies
        in alphabetical order. Variations are to track sequences of two words and their frequencies, or n
        words and their frequencies.

* * * * * ============================================================================================= * * * * *

Solution:
    Display result:
        Enter the input file name: ../fileTest/testProj7.txt
        After 1
        Define 2
        Employ 1
        Explain 2
        Use 1
        a 4
        able 1
        and 3
        are 1
        assign 1
        be 1
        chapter, 1
        code 1
        completing 1
        design 1
        effectively 1
        exploit 1
        filtering, 1
        for 1
        function 2
        functions 3
        higher-order 1
        in 3
        it 1
        mapping, 1
        namespace 1
        of 1
        optional 1
        parameters 1
        program 2
        recursive 1
        reducing 1
        required 1
        structuring 1
        tasks 1
        the 2
        this 1
        to 3
        top-down 1
        use 1
        useful 1
        why 1
        will 1
        with 1
        you 1

"""


inName = input("Enter the input file name: ")

inputFile = open(inName, 'r')
uniqueWords = {}

for line in inputFile:
    words = line.split()
    for word in words:
        freq = uniqueWords.get(word, None)
        if freq == None:
            uniqueWords[word] = 1
        else:
            uniqueWords[word] = freq + 1


words = list(uniqueWords.keys())
words.sort()
for word in words:
    print(word, uniqueWords[word])
