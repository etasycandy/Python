"""
Author: Tran Dinh Hoang
Date: 16/08/2021
Program: Project_10_page166.py
Problem:
    10. Conversations often shift focus to earlier topics. Modify the therapist program to support this
        capability. Add each patient input to a history list. Then, occasionally choose an element at
        random from this list, change persons, and prepend (add at the beginning) the qualifier 'Earlier
        you said that' to this reply. Make sure that this option is triggered only after several exchanges
        have occurred.

* * * * * ============================================================================================= * * * * *

Solution:
    Display result:


"""
import random

history = []

hedges = ("Please tell me more.",
          "Many of my patients tell me the same thing.",
          "Please continue.")

qualifiers = ("Why do you say that ",
              "You seem to think that ",
              "Can you explain why ")

replacememts = {
    "I": "you", "me": "you", "my": "your",
    "we": "you", "us": "you", "mine": "yours",
    "you": "I", "your": "my", "yours": "mine"
}

def reply(sentence):
    probability = random.randint(1, 5)
    if probability in (1, 2):
        answer = random.choice(hedges)
    elif probability == 3 and len(history) > 3:
        answer = "Earlier you said that " + changePerson(random.choice(history))
    else:
        answer = random.choice(qualifiers) + changePerson(sentence)
    history.append(sentence)
    return answer


def changePerson(sentence):
    words = sentence.split()
    replyWords = []
    for word in words:
        replyWords.append(replacememts.get(word, word))
    return " ".join(replyWords)


def main():
    print("Good morning, I hope you are well today.")
    print("What can I do for you?")
    while True:
        sentence = input("\n>> ")
        if sentence.upper() == "QUIT":
            print("Have a nice day!")
            break
        print(reply(sentence))


if __name__ == '__main__':
    main()


