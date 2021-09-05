"""
Author: Tran Dinh Hoang
Date: 30/08/2021
Program: Exercise_07_page_182.py
Problem:

    7.  Explain what happens when the following recursive function is called with the values "hello" and 0
        as arguments:
            def example(aString, index):
               if index == len(aString):
                   return ""
                else:
                   return aString[index] + example(aString, index + 1)

* * * * * ============================================================================================= * * * * *

Solution:
    Result:
        -   Print to the screen the characters at the index position until the index is equal to the length
            of the array. In this case, we get the input string

"""

# ex:

def example(aString, index):
    if index == len(aString):
        return ""
    else:
        return aString[index] + example(aString, index + 1)


def main():
    print(example("hello", 0))


if __name__ == '__main__':
    main()
