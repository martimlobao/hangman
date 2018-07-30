# Basic hangman game
# Written by Martim Lobao, Katrina Miller, and Samuel Dallal
#
# https://git.generalassemb.ly/ + user
# for user in [martim, katrina-miller-ga-2, SamuelDallal]


import random
import requests


def get_words():
    # Warning: this word list includes swears!
    url = 'https://raw.githubusercontent.com/first20hours/google-10000-english/master/20k.txt'
    try:
        word_list = requests.get(url).text.split()
    except Exception as e:
        print('Oh no, we couldn\'t download the entire word list with 20 thousand words!')
        print('You had an error: ', e)
        print('Attempting to load local word list file.')
        try:
            with open('20k.txt') as f:
                word_list = f.read().split()
        except Exception as e:
            print('Couldn\'t load local word list, we\'ll use a much smaller word list instead.')
            word_list = ['time', 'person', 'year', 'way', 'day', 'thing', 'man', 'world', 'life',
                         'hand', 'part', 'child', 'eye', 'woman', 'place', 'work', 'week', 'case',
                         'point', 'government', 'company', 'number', 'group', 'problem', 'fact']
    return word_list


def pick_word(word_list):
    return random.choice(word_list).upper()


def fresh_state(word):
    state = ''
    for character in word:
        state += '_'
    return state


def next_state(word, current_state, guess):
    new_state = ''
    for ind, character in enumerate(word):
        if character.upper() == guess.upper():
            new_state += guess.upper()
        else:
            new_state += current_state[ind]
    return new_state


def print_state(state):
    printable = ''
    for character in state:
        printable += character + ' '
    print(printable)


def is_game_over(wrong_guesses):
    if len(wrong_guesses) >= 6:
        return True
    else:
        return False


def print_wrong(wrong_guesses):
    if len(wrong_guesses) <= 0:
        print('''
           ______
           |    |
                |
                |
                |
              __|__''')
    elif len(wrong_guesses) == 1:
        print('''
           ______
           |    |
           o    |
                |
                |
              __|__''')
    elif len(wrong_guesses) == 2:
        print('''
           ______
           |    |
           o    |
           |    |
                |
              __|__''')
    elif len(wrong_guesses) == 3:
        print('''
           ______
           |    |
           o    |
          -|    |
                |
              __|__''')
    elif len(wrong_guesses) == 4:
        print('''
           ______
           |    |
           o    |
          -|-   |
                |
              __|__''')
    elif len(wrong_guesses) == 5:
        print('''
           ______
           |    |
           o    |
          -|-   |
          /     |
              __|__''')
    else:
        print('''
           ______
           |    |
           o    |
          -|-   |
          / \   |
              __|__''')
    print(f'\nWrong guesses: {wrong_guesses}\n')


def play_hangman():
    word_list = get_words()
    while True:
        print("\nLet's play hangman!\n")
        word = pick_word(word_list)
        wrong_guesses = []
        current_state = fresh_state(word)
        print_state(current_state)

        while current_state != word and not is_game_over(wrong_guesses):
            guess = input('\nMake a guess: ').upper()
            if (guess not in word) and (guess not in wrong_guesses) and guess != word:
                wrong_guesses.append(guess)
            elif guess == word:
                print('\nYou win!')
                break
            current_state = next_state(word, current_state, guess)
            print_wrong(wrong_guesses)
            print_state(current_state)
            if is_game_over(wrong_guesses):
                print('\nYou lose!')
                print(f'The word was {word}.')
                break

        if not is_game_over(wrong_guesses) and not guess == word:
            print('\nYou win!')

        keep_going = input('\nPlay again? (y/n) ').upper()
        while keep_going not in ('Y', 'N'):
            keep_going = input('\nPlay again? (y/n) ').upper()

        if keep_going == 'N':
            print('\nThanks for playing!')
            break


if __name__ == '__main__':
    play_hangman()
