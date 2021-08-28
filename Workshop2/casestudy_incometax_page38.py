"""
Author: Trần Đình Hoàng
Date: 12/07/2021
Program: casestudy_incometax_page_38.py
Problem:
    *   Handling customer requests:
        -   The customer requests a program that computes a person’s income tax.

    *   Analyze customer requirements:
        -   All taxpayers are charged a flat tax rate of 20%.
        -   All taxpayers are allowed a $10,000 standard deduction.
        -   For each dependent, a taxpayer is allowed an additional $3,000 deduction.
        -   Gross income must be entered to the nearest penny.
        -   The income tax is expressed as a decimal number.

Solution:
    Display result:

        Enter the gross income: 150000
        Enter the number of dependents: 3
        The income tax is $26200.0

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
print("The income tax is $" + str(incomeTax))
