"""
Author: Trần Đình Hoàng
Date: 12/07/2021
Program: project_03_page_62.py
Problem:
    3.  Five Star Retro Video rents VHS tapes and DVDs to the same connoisseurs who
        like to buy LP record albums. The store rents new videos for $3.00 a night, and
        oldies for $2.00 a night. Write a program that the clerks at Five Star Retro Video
        can use to calculate the total charge for a customer’s video rentals. The program
        should prompt the user for the number of each type of video and output the total
        cost.

Solution:
    Display result:
        1. New disc : $3.00 & 5 discs left.
        2. Old disc : $2.00 & 10 discs left.
        Choose the type of disc you want to rent: 1
        Number of discs you want to rent: 5

        The amount you have to pay: $15.00

"""
# giá cho thuê
priceOld = 2
quantityOld = 10
priceNew = 3
quantityNew = 5

# input
discType = int(input("1. New disc : $" + str(priceNew) + ".00 & " + str(quantityNew) + " discs left."                  
                     "\n2. Old disc : $" + str(priceOld) + ".00 & " + str(quantityOld) + " discs left."
                     "\nChoose the type of disc you want to rent: "))
quantity = int(input("Number of discs you want to rent: "))

# cal
if discType == 1:
    if quantity > quantityNew:
        print("\nSorry! The number of discs is not enough.")
    else:
        price = priceNew * quantity
        print("\nThe amount you have to pay: $" + str(price) + ".00")

if discType == 2:
    if quantity > quantityOld:
        print("\nSorry! The number of discs is not enough.")
    else:
        price = priceOld * quantity
        print("\nThe amount you have to pay: $" + str(price) + ".00")


