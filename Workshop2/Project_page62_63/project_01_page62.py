"""
Author: Trần Đình Hoàng
Date: 12/07/2021
Program: project_01_page_62.py
Problem:
    1.  The tax calculator program of the case study outputs a floating-point number
        that might show more than two digits of precision. Use the round function to
        modify the program to display at most two digits of precision in the output number.

Solution:
    Display result:
        Enter the gross income: 112325457
        Enter the number of dependents: 5
        The income tax is $22460091.4

"""

# Initialize the constants

# Tỉ lệ thuế xuất 20% = 0.2
TAX_RATE = 0.2
# Khấu trừ tiêu chuẩn
STANDARD_DEDUCTION = 10000
# Khoảng trừ phụ thuộc
DEPENDENT_DEDUCTION = 3000

# Request the inputs

# Tổng thu nhập
grossIncome = float(input("Enter the gross income: "))
# Số người phụ thuộc
numDependents = int(input("Enter the number of dependents: "))

# Compute the income tax
taxableIncome = grossIncome - STANDARD_DEDUCTION - DEPENDENT_DEDUCTION * numDependents
incomeTax = taxableIncome * TAX_RATE
# Display the income tax
print("The income tax is $" + str(round(incomeTax, 2)))
