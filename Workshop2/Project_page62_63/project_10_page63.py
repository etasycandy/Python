"""
Author: Trần Đình Hoàng
Date: 12/07/2021
Program: project_10_page_63.py
Problem:
    10. An employee’s total weekly pay equals the hourly wage multiplied by the total
        number of regular hours plus any overtime pay. Overtime pay equals the total
        overtime hours multiplied by 1.5 times the hourly wage. Write a program that
        takes as inputs the hourly wage, total regular hours, and total overtime hours and
        displays an employee’s total weekly pay.

Solution:
    Display result:
        Enter of hourly wages: 18000
        Enter of regular hour: 123
        Enter of over time: 23

        Total salary = 2835000 vnđ

"""
hourlyWages = float(input("Enter of hourly wages: "))
regularHour = float(input("Enter of regular hour: "))
overTime = float(input("Enter of over time: "))

overTimePay = (hourlyWages * 1.5) * overTime
regularPay = hourlyWages * regularHour

totalPay = overTimePay + regularPay

# print
print("\nTotal salary = " + str(round(totalPay)) + " vnđ")
