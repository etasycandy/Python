"""
Author: Trần Đình Hoàng
Date: 17/07/2021
Program: casestudy_anInvestmentReport_page73.py
Problem:
    Compute an investment report.
        1. The inputs are starting investment amount number of years interest rate (an integer percent)
        2. The report is displayed in tabular form with a header.
        3. Computations and outputs:
            -   for each year compute the interest and add it to the investment print a formatted row
                of results for that year
        4. The ending investment and interest earned are also

Solution:
    Display result:

        Enter the investment amount: 10000
        Enter the number of years: 5
        Enter the rate as a %: 5
        Year  Starting balance  Interest  Ending balance
           1          10000.00    500.00        10500.00
           2          10500.00    525.00        11025.00
           3          11025.00    551.25        11576.25
           4          11576.25    578.81        12155.06
           5          12155.06    607.75        12762.82
        Ending balance: $12762.82
        Total interest earned: $2762.82

"""

# Accept the inputs
startBalance = float(input("Enter the investment amount: "))
years = int(input("Enter the number of years: "))
rate = int(input("Enter the rate as a %: "))

# Convert the rate to a decimal number
rate = rate / 100

# Initialize the accumulator for the interest
totalInterest = 0.0

# Display the header for the table
print("%4s%18s%10s%16s" % ("Year", "Starting balance", "Interest", "Ending balance"))

# Compute and display the results for each year
for year in range(1, years + 1):
    interest = startBalance * rate
    endBalance = startBalance + interest
    print("%4d%18.2f%10.2f%16.2f" % (year, startBalance, interest, endBalance))
    startBalance = endBalance
    totalInterest += interest

# Display the totals for the period
print("Ending balance: $%0.2f" % endBalance)
print("Total interest earned: $%0.2f" % totalInterest)
