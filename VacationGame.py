# Importing all the necessary libraries
from time import sleep
import messages
import os


# Help-function to print game-prompts
def textOutput(textInput):
    for s in textInput:
        print(s);
        sleep(2)


# Help-function to check if a word exists in English
def checkValid(file, word):
    with open(file, encoding='utf-8') as read_obj:
        for line in read_obj:
            if word in line:
                return True
    return False

def main():
    # Start interaction with the user
    # Check if the name is valid
    user_name = input(messages.GREETING)
    flag = True
    while flag:
        name = user_name.lower()
        if name.isalpha():
            flag = False
            print(messages.GREET_USER.format(user_name))
        else:
            user_name = input(messages.NAME_ERROR)

    # Explain the rules of the game
    textOutput(messages.GAME_RULES)

    # Keep track of correct and incorrect answers
    choices = []
    guesses = 0
    fileWords = 'words_database.csv'
    while len(choices) < 3:
        user_answer = input(messages.GAME_QUESTION)
        answer = user_answer.lower()
        words_total = checkValid(fileWords, answer)
        # Not a valid answer
        if (words_total is False) or (answer.isalpha() is False):
            print(messages.ANSWER_ERROR_NO_WORD)
            continue

        # Correct answer
        # TODO: switch cases for different puzzles (word length, last letter, next letter in the alphabet)
        elif name[0] == answer[0]:
            if answer not in choices:
                choices.append(answer)
                print(messages.ANSWER_SUCCESS)
            else:
                print(messages.ANSWER_ERROR_DUBLE.format(answer))

        # Wrong answer
        else:
            guesses += 1
            print(messages.ANSWER_WRONG)
            if guesses == 4:
                hint = input(messages.HINT)
                if hint == "y" or hint =="yes" or hint == "ja" or hint == "yep":
                    guesses = 0
                    print(messages.ANSWER_EXAMPLE)
                guesses = 0

    print(messages.WINNER.format(choices[0], choices[1], choices[2]))

main()
