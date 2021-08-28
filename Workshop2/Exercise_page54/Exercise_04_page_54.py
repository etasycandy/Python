"""
Author: Trần Đình Hoàng
Date: 12/07/2021
Program: Exersice_04_page_54.py
Problem:
    4.  How does a Python programmer concatenate a numeric value to a string value?

Solution:
    To concatenate a numeric value with a literal value we add ',' between them
    Or if you want to use '+' to replace ',' then you must convert the number to a string with str()

    Ex:
        Display result:    ('Birth of year:', 2000)
                            Birthday: 21
"""

birthOfYear = "Birth of year:", 2000
Birthday = "Birthday: " + str(21)

print(birthOfYear)
print(Birthday)

