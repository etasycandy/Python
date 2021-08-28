"""
Author: Trần Đình Hoàng
Date: 19/07/2021
Program: project_07_page100.py
Problem:
    7.  Teachers in most school districts are paid on a schedule that provides a salary based on their number of years
        of teaching experience. For example, a beginning teacher in the Lexington School District might be paid $30,000
        the first year. For each year of experience after this first year, up to 10 years, the teacher receives a 2%
        increase over the preceding value. Write a program that displays a salary schedule, in tabular format, for
        teachers in a school district. The inputs are the starting salary, the percentage increase, and the number of
        years in the schedule. Each row in the schedule should contain the year number and the salary for that year.

Solution:
    Display result:
        Enter starting salary: $ 5000
        Enter salary increase rate: 2
        Enter years of service: 8

              Year      Starting salary      Salary increase rate      Ending salary
                1              $ 5000.0                2%                   $ 5100.0
                2              $ 5100.0                2%                   $ 5202.0
                3              $ 5202.0                2%                   $ 5306.0
                4              $ 5306.0                2%                   $ 5412.2
                5              $ 5412.2                2%                   $ 5520.4
                6              $ 5520.4                2%                   $ 5630.8
                7              $ 5630.8                2%                   $ 5743.4
                8              $ 5743.4                2%                   $ 5858.3

"""
def checkYear(year):
    while not 0 < year < 11:
        year = float(input("Enter years of service: "))

# input
salary = float(input("Enter starting salary: $ "))

rate = float(input("Enter salary increase rate: "))

year = int(input("Enter years of service: "))
checkYear(year)


print("\n%10s %20s %25s %18s" % ("Year", "Starting salary", "Salary increase rate", "Ending salary"))

for i in range(1, year+1):
    endSalary = salary + (salary * rate/100)
    print("%9s %21s %17s %26s" % (i, "$ " + str(round(salary, 1)), str(round(rate))+"%", "$ " + str(round(endSalary, 1))))
    salary = endSalary

