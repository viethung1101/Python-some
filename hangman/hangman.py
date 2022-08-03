#! /usr/bin/env python3

from words import words
import random
import string
def get_valid_word(words):
    """randomly chooses valid word from the list and return it in uppercase"""
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()
    #what current word is

    lives = 6
    while len(word_letters) > 0 and lives > 0:
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("")
        print("You have used these letters : ", ' '.join(used_letters))
        print("Current word: ", ' '.join(word_list))
        print("lives left: ", lives)
        #get the user input
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                print("Your char is not in word!")
                lives -= 1
        elif user_letter in used_letters:
            print("You have already use that letter!. Try again.")
        else:
            print("Invalid character. Try again!")

    if lives == 0:
        print("You lose! the word is ", word)
    else:
        print("Congrate!!")

hangman()
