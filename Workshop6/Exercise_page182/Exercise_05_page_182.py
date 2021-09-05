"""
Author: Tran Dinh Hoang
Date: 30/08/2021
Program: Exercise_05_page_182.py
Problem:

    5.  Explain what happens when the following recursive function is called with the value 4 as an argument:
            def example(n):
                if n > 0:
                    print(n)
                    example(n)
                else:
                    example(n - 1)

* * * * * ============================================================================================= * * * * *

Solution:
    Result:
        -   Falls into a cyclic infinite loop because the stopping condition is not true

"""
# ex:

def example(n):
    if n > 0:
        print(n)
        example(n)
    else:
        example(n - 1)


def main():
    example(4)


if __name__ == '__main__':
    main()