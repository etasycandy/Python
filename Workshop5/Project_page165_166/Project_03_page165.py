"""
Author: Tran Dinh Hoang
Date: 16/08/2021
Program: Project_03_page165.py
Problem:
    3.  Modify the sentence-generator program of Case Study 5.3 so that it inputs its vocabulary from a set of text
        files at startup. The filenames are nouns.txt, verbs.txt, articles.txt, and prepositions.txt. (Hint: Define
        a single new function, getWords. This function should expect a filename as an argument. The function should
        open an input file with this name, define a temporary list, read words from the file, and add them to the
        list. The function should then convert the list to a tuple and return this tuple. Call the function with
        an actual filename to initialize each of the four variables for the vocabulary.)

* * * * * ============================================================================================= * * * * *

Solution:
    Display result
        Enter the number of sentences: 2
        THE BAT SAW A BAT BY THE BAT
        THE BOY SAW A BAT BY A BAT

"""
import random


def getWords(fileName):
    inputFile = open(fileName, 'r')
    words = []
    for line in inputFile:
        words.extend(line.split())
    return tuple(words)


articles = getWords("../fileTest/articles.txt")

nouns = getWords("../fileTest/nouns.txt")

verbs = getWords("../fileTest/verbs.txt")

preposition = getWords("../fileTest/preposition.txt")


def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()


def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)


def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + prepositionalPhrase()


def prepositionalPhrase():
    return random.choice(preposition) + " " + nounPhrase()

def main():
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())


main()
