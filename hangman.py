import random
from test.word.word import words

def word(words):
    word = random.choice(words)
    while '-' in word or '.' in word or len(word) < 3 or ' ' in word:
        word = random.choice(words)
    return word

def hangman():
    guess_word = word(words)

    while len(guess_word) != 0:
        

    







