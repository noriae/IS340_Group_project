from operator import truediv
import random


words=['chicken', 'dog', 'cat', 'rabbit', 'mouse', 'frog']
lives_remaining = 9
guessed_letters= ''


def select_a_word():
    pos = random.randint(0, len(words) - 1)
    return words[pos]

def get_a_guess(word):
    print_word_with_blanks(word)
    print('Lives Remaining: ' + str(lives_remaining))
    guess = input(' Guess a letter or whole word ?')
    return guess

def print_word_with_blanks(word):
    display_word = ''
    for letter in word:
        if guessed_letters.find(letter) > -1:
            display_word = display_word + letter
        else:
            display_word = display_word + '-'
    print(display_word)
    
def process_guess(guess, word):
    if len(guess) > 1 and len(guess) == len(word):
        return whole_word_guess(guess, word)
    else:
        return single_letter_guess(guess, word)
    
def whole_word_guess(guess, word):
    global lives_remaining
    if guess.lower() == word.lower():
        return True
    else:
        lives_remaining - 1
        return False
    
def single_letter_guess(guess, word):
    global guessed_letters
    global lives_remaining
    if word.find(guess) == -1:
        lives_remaining -= 1
    guessed_letters += guess.lower()
    if all_letters_guessed(word):
        return True
    return False

def all_letters_guessed(word):
    for letter in word:
        if guessed_letters.find(letter.lower()) == -1:
            return False
    return True

def hangman():
    word = select_a_word()
    while True:
        guess = get_a_guess(word)
        if process_guess(guess, word):
            print('You win!')
            break
        if process_guess(guess, word) != False:
            print('You are Hung!')
            print('The word was: ' + word)
            break
        


if __name__ == "__main__":
    hangman = hangman()