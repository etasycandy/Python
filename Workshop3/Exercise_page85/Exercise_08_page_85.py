"""
Author: Trần Đình Hoàng
Date: 17/07/2021
Program: Exercise_08_page_85.py
Problem:
    8.  The variables x and y refer to numbers. Write a code segment that prompts the user for
        an arithmetic operator and prints the value obtained by applying that operator to x and y.

Solution:
    Display result:
        Choose:  (1) to perform math (+)
                 (2) to perform math (-)
                 (3) to perform math (*)
                 (4) to perform math (:)
                 (5) to perform math (mod)
                 (6) to perform math (^)
                 (7) to perform math (:)
                 (0) to ExitEnter your selection: 8
        Enter your selection: -2
        Enter your selection: 3
        10 * 5 = 50

"""

x = 10
y = 5


def switch(i):
    switcher = {
        1: str(x) + " + " + str(y) + " = " + str(x + y),
        2: str(x) + " - " + str(y) + " = " + str(x - y),
        3: str(x) + " * " + str(y) + " = " + str(x * y),
        4: str(x) + " : " + str(y) + " = " + str(x / y),
        5: str(x) + " mod " + str(y) + " = " + str(x % y),
        6: str(x) + " ^ " + str(y) + " = " + str(x ** y),
        7: str(x) + " : " + str(y) + " = " + str(x // y),
        0: "Bye"
    }
    return switcher.get(i)


def checkValid(i):
    while (i < 0 or i > 7):
        i = int(input("Enter your selection: "))
    print(switch(i))


i = int(input("Choose:  (1) to perform math (+)"
              "\n         (2) to perform math (-)"
              "\n         (3) to perform math (*)"
              "\n         (4) to perform math (:)"
              "\n         (5) to perform math (mod)"
              "\n         (6) to perform math (^)"
              "\n         (7) to perform math (:)"
              "\n         (0) to Exit"
              "Enter your selection: "))
checkValid(i)
