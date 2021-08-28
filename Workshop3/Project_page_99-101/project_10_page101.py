"""
Author: Trần Đình Hoàng
Date: 19/07/2021
Program: project_10_page101.py
Problem:
    10. The credit plan at TidBit Computer Store specifies a 10% down payment and an annual interest rate of 12%.
        Monthly payments are 5% of the listed purchase price, minus the down payment. Write a program that takes the
        purchase price as input. The program should display a table, with appropriate headers, of a payment schedule
        for the lifetime of the loan. Each row of the table should contain the following items:

        -   the month number (beginning with 1)
        -   the current total balance owed
        -   the interest owed for that month
        -   the amount of principal owed for that month
        -   the payment for that month
        -   the balance remaining after payment

        The amount of interest for a month is equal to balance * rate / 12. The amount of principal for a month
        is equal to the monthly payment minus the interest owed.

Solution:
    Display result:


"""

price = int(input("Enter the purchase price: "))

rate = 12/100

payment = price * 5 / 100

print("%10s %30s %18s %19s %13s %23s" % ("Month", "Starting Balance", "Interest to Pay", "Principal to Pay", "Payment", "Ending Balance"))

startBalance = price
month = 1
while startBalance != 0:
    interest = startBalance * rate / 12
    principal = payment - interest
    endingBalance = startBalance - payment
    print("%10s %30.2f %18.2f %19.2f %13.2f %23.2f" % (month, startBalance, interest, principal, payment, endingBalance))
    month += 1
    startBalance = endingBalance
