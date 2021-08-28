"""
Author: Tran Dinh Hoang
Date: 07/08/2021
Program: CaseStudy_GeneratingSentences_page150.py
Problem:

    Write a program that generates sentences.

* * * * * ============================================================================================= * * * * *

Solution:
    Display result:
        Enter the number of sentences: 3
        A BAT HIT THE GIRL BY A BAT
        THE GIRL SAW THE BAT WITH A BOY
        A BAT HIT A BALL WITH A BAT

"""


import random
# Vocabulary: words in 4 different parts of speech
articles = ("A", "THE")
nouns = ("BOY", "GIRL", "BAT", "BALL")
verbs = ("HIT", "SAW", "LIKED")
prepositions = ("WITH", "BY")
def sentence():
    """Builds and returns a sentence."""
    return nounPhrase() + " " + verbPhrase()


def nounPhrase():
    """Builds and returns a noun phrase."""
    return random.choice(articles) + " " + random.choice(nouns)


def verbPhrase():
    """Builds and returns a verb phrase."""
    return random.choice(verbs) + " " + nounPhrase() + " " + \
    prepositionalPhrase()


def prepositionalPhrase():
    """Builds and returns a prepositional phrase."""
    return random.choice(prepositions) + " " + nounPhrase()


def main():
    """Allows the user to input the number of sentences
    to generate."""
    number = int(input("Enter the number of sentences: "))
    for count in range(number):
        print(sentence())


if __name__ == '__main__':
    main()

