"""
Author: Tran Dinh Hoang
Date: 31/07/2021
Program: Exersice_01_page_125.py
Problem:
    1.  Write a code segment that opens a file named myfile.txt for input and prints the number of lines in the file.

* * * * * ============================================================================================= * * * * *

Solution:
    Display result:
        Content first 5 characters: Hoàng

"""

textFile = open("../fileTest/myfile.txt", 'w', encoding='utf-8')
textFile.write("Hoàng là nhất"
               "\nFirst line"
               "\nSecond line"
               "\nThird line")

textFile = open("../fileTest/myfile.txt.txt", 'r', encoding='utf-8')
print(textFile)

count = 0
for line in textFile:
    count += 1

print("The number of lines: ", count)

textFile.close()



