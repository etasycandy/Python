"""
Author: Tran Dinh Hoang
Date: 05/08/2021
Program: Casestudy_textAnalysis_page126.py
Problem:

    Write a program that computes square roots.

* * * * * ============================================================================================= * * * * *

Solution:
    Enter the file name: ./fileTest/myText.txt
    debug_text: Because our initial estimate is 1.0, the loop must compute at least one new estimate.
    Therefore, we use a while True loop. This loop transforms the estimate before
    determining whether it is close enough to the tolerance value to stop the process.
    The process should stop when the difference between the square of our estimate and
    the original number becomes less than or equal to the tolerance value. Note that this
    difference may be positive or negative, so we use the abs function to obtain its absolute value before examining it.
    debug_sentences: 6
    debug_words: 91
    The Flesch Index is 51.9902838827839
    The Grade Level Equivalent is 10
    6 sentences
    91 words
    150 syllables

"""



# Take the inputs
fileName = input("Enter the file name: ")
inputFile = open(fileName, 'r')
# inputFile = open("./fileTest/myText.txt", 'r', encoding='utf-8')
text = inputFile.read()

print(f"debug_text: {text}")

# Count the sentences
sentences = text.count('.') + text.count('?') + \
            text.count(':') + text.count(';') + \
            text.count('!')

print(f"debug_sentences: {sentences}")

# Count the words
words = len(text.split())

print(f"debug_words: {words}")

# Count the syllables
syllables = 0
# vowels = "aeiouAEIOU"
for word in text.split():
    for vowel in ['a', 'e', 'i', 'o', 'u']:
        syllables += word.count(vowel)
    for ending in ['es', 'ed', 'e']:
        if word.endswith(ending):
            syllables -= 1
    if word.endswith('le'):
        syllables += 1

# Compute the Flesch Index and Grade Level
index = 206.835 - 1.015 * (words / float(sentences)) - 84.6 * (syllables / words)
level = int(round(0.39 * (words / float(sentences)) + 11.8 * (syllables / float(words)) - 15.59))

# Output the results
print("The Flesch Index is", index)
print("The Grade Level Equivalent is", level)
print(sentences, "sentences")
print(words, "words")
print(syllables, "syllables")
