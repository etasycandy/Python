"""
Author: Trần Đình Hoàng
Date: 17/07/2021
Program: Exercise_01_page_92.py
Problem:
    1.  Translate the following for loops to equivalent while loops:
        a.  for count in range(100):
                print(count)
        b.  for count in range(1, 101):
                print(count)
        c.  for count in range(100, 0, -1):
                print(count)

Solution:

"""
# 1
countA = 0
while (0 <= countA < 100):
    print(countA)
    countA += 1

# 2
countB = 1
while (0 < countB < 101):
    print(countB)
    countB += 1

# 3
countC = 100
while (0 < countC <= 100):
    print(countC)
    countC -= 1

