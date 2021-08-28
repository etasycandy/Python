"""
Author: Trần Đình Hoàng
Date: 17/07/2021
Program: Exercise_04_page_73.py
Problem:
    4.  Write a loop that outputs the numbers in a list named salaries. The outputs should be formatted
        in a column that is right-justified, with a field width of 12 and a precision of 2.

Solution:
    Display result:
              100.57
              200.46
              300.12
              400.32

"""

salaries = [100.5665, 200.457, 300.123, 400.321]

for i in salaries:
    print(f"{i:12.2f}")
    # or
    # print("%12.2f" % i)
