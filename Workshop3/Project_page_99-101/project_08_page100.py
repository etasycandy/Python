"""
Author: Trần Đình Hoàng
Date: 19/07/2021
Program: project_08_page100.py
Problem:
    8.  The greatest common divisor of two positive integers, A and B, is the largest number that can be evenly divided
        into both of them. Euclid’s algorithm can be used to find the greatest common divisor (GCD) of two positive
        integers. You can use this algorithm in the following manner:

        a.  Compute the remainder of dividing the larger number by the smaller number.
        b.  Replace the larger number with the smaller number and the smaller number with the remainder.
        c.  Repeat this process until the smaller number is zero.

        The larger number at this point is the GCD of A and B. Write a program that lets the user enter two integers
        and then prints each step in the process of using the Euclidean algorithm to find their GCD.

Solution:
    Display result:
        Enter the number of iterations: 5
        π/4 =  0.7853981633974483
        The result after 5 iterations is 0.8349206349206351

"""

# Find the GCD of two positive numbers a & b
# Input a and b
a = int(input("Input the number a: "))
b = int(input("Input the number b: "))
# Catch error inputing wrong type of number
while a | b < 0:
    print("Please input two positive integer numbers!")
    a = int(input("a: "))
    b = int(input("b: "))
# Save the current value of a & b for printing the result conclusion ***
A = a
B = b

# Compute the remainder
print("Step 1: Compute the remainder of dividing the larger number by the smaller number...")
remainder = a % b if a > b else b % a
print('Remainder of', a, 'and', b, 'is', remainder)

# Find the GCD
if remainder == 0:
    gcd = b if a > b else a
    if a > b:
        print('Because', a, 'is divisible by', b, 'so:')
    else:
        print('Because', b, 'is divisible by', a, 'so:')
else:
    print('Step 2: Replace the larger number with the smaller number and the smaller number with the remainder & Repeat this process until the smaller number is zero...')
    print('The larger number at this point is the GCD of A and B\n')
    print('%1s %24s %27s %24s' % ('Process','Larger number', 'Smaller number', 'Remainder\n'))
    print('Start...')
    print('%25s %28s %26s' % (a if a > b else b, b if a > b else a, a > b and a % b or b % a))
    print('Change...')
    print('%25s %28s' % (b if a > b else a, remainder))
    while not remainder == 0:
        if a > b:
            a = b
            b = remainder
            remainder = a % b
            gcd = b
            print('%25s %28s %26s' % (a, b, remainder))
            print('Change...')
            print('%25s %28s' % (b, remainder))
        else:
            b = a
            a = remainder
            remainder = b % a
            gcd = a
            print('%25s %28s %26s' % (b, a, remainder))
            print('Change...')
            print('%25s %28s' % (a, remainder))
    print('The program stops when the Smaller number = 0, at this point the larger number', gcd, 'is the GCD of two number', A, 'and', B)
print('===============')
# result conclusion ***
print('GCD OF NUMBER', A, 'AND NUMBER', B, 'IS', gcd)
