"""
Author: Tran Dinh Hoang
Date: 16/08/2021
Program: Project_01_page165.py
Problem:
    1.  A group of statisticians at a local college has asked you to create a set of functions that compute the
        median and mode of a set of numbers, as defined in Section 5.4. Define these functions in a module named
        stats.py. Also include a function named mean, which computes the average of a set of numbers. Each function
        should expect a list of numbers as an argument and return a single number. Each function should return 0
        if the list is empty. Include a main function that tests the three statistical functions with a given list.

* * * * * ============================================================================================= * * * * *

Solution:
    Display result
        List: [3, 1, 7, 1, 4, 10]
        Mode: 1
        numbers: [1, 1, 3, 4, 7, 10]
        Median: 3.5
        Mean: 4.333333333333333

"""

def mean(lyst):
    """Returns the mean of a list of numbers."""
    sum = 0
    for number in lyst:
        sum += number
    if len(lyst) == 0:
        return 0
    else:
        return sum / len(lyst)


def mode(lyst):
    """Returns the mode of a list of numbers."""
    theDictionary = {}
    for number in lyst:
        freq = theDictionary.get(number, None)
        if freq == None:
            theDictionary[number] = 1
        else:
            theDictionary[number] = freq + 1
    # print(f"theDictionary: {theDictionary}")

    if len(theDictionary) == 0:
        return 0
    else:
        theMaximum = max(theDictionary.values())
        for key in theDictionary:
            if theDictionary[key] == theMaximum:
                return key


def median(lyst):
    """Returns the median of a list of numbers."""
    numbers = []
    for number in lyst:
        numbers.append(number)

    numbers.sort()
    print(f"numbers: {numbers}")
    if len(numbers) == 0:
        return 0
    else:
        midpoint = len(numbers) // 2
        if len(numbers) % 2 == 1:
            return numbers[midpoint]
        else:
            return (numbers[midpoint] + numbers[midpoint - 1]) / 2


def main():
    """Tests the functions."""
    lyst = [3, 1, 7, 1, 4, 10]
    print("List:", lyst)
    print("Mode:", mode(lyst))
    print("Median:", median(lyst))
    print("Mean:", mean(lyst))


if __name__ == '__main__':
    main()

