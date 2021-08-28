"""
Author: Trần Đình Hoàng
Date: 17/07/2021
Program: project_04_page99.py
Problem:
    4.  A standard science experiment is to drop a ball and see how high it bounces. Once
        the “bounciness” of the ball has been determined, the ratio gives a bounciness index.
        For example, if a ball dropped from a height of 10 feet bounces 6 feet high, the index
        is 0.6, and the total distance traveled by the ball is 16 feet after one bounce. If the
        ball were to continue bouncing, the distance after two bounces would be 10ft + 6ft +6ft +3.6ft = 25.6 ft.
        Note that the distance traveled for each successive bounce is the distance to the floor
        plus 0.6 of that distance as the ball comes back up. Write a program that lets the user
        enter the initial height from which the ball is dropped and the number of times the ball
        is allowed to continue bouncing. Output should be the total distance traveled by the ball.

Solution:
    Display result:
        Enter initial height: 10
        Enter the height of the bounce ball after release: 6
        Enter the number of times the ball bounces: 2
        Total distance traveled is: 25.6 units.

"""

heightInitial = float(input("Enter initial height: "))
heightBounciness = float(input("Enter the height of the bounce ball after release: "))
numOfBallBounces = int(input("Enter the number of times the ball bounces: "))
index = heightBounciness / heightInitial
street = 0

while numOfBallBounces > 0:
    street += heightInitial
    heightInitial *= index
    street += heightInitial
    numOfBallBounces -= 1

print("Total distance traveled is:", street, "units.")
