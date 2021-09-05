"""
Author: Tran Dinh Hoang
Date: 30/08/2021
Program: Exercise_06_page_182.py
Problem:

    6.  Explain what happens when the following recursive function is called with the values "hello" and 0
        as arguments:
            def example(aString, index):
               if index < len(aString):
                 example(aString, index + 1)
                 print(aString[index], end = "")

* * * * * ============================================================================================= * * * * *

Solution:
    Result:
        -   Print to the screen from the last character of the string to the first character (reverse the string)

"""
# ex:

def example(aString, index):
    if index < len(aString):
        example(aString, index + 1)
        print(aString[index], end="")


def main():
    example("hello", 0)


if __name__ == '__main__':
    main()