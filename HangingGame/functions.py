# -*- coding:utf-8 -*-
"""
All functions used for the hanging game are here
"""
import pickle
import random

def register_gamer():
    """
    Read the scores file.
    If the gamer is not register yet, we create her/his profile
    Else we retrieved gamer's informations (pseudo and score)
    """

    pseudo = input('==> Please type your pseudo: ')

    try:
        with open('scores', mode='rb') as scores_file:
            depickler_file = pickle.Unpickler(scores_file)
            gamers = depickler_file.load()
            assert pseudo in gamers # First we search the gamer in 'scores' file
            score = gamers[pseudo]
    except OSError: # The file 'scores' doesn't exist
        with open('scores', mode='xb') as scores_file:
            pickler_file = pickle.Pickler(scores_file)
            score = 0
            gamers = {pseudo: score}
            pickler_file.dump(gamers)
    except AssertionError: # The player doesn't exist yet in 'score file'
        with open('scores', mode='wb') as scores_file:
            pickler_file = pickle.Pickler(scores_file)
            score = 0
            gamers[pseudo] = score
            pickler_file.dump(gamers)

    return pseudo, score

def get_word():
    """
    The program reach a word from 'dictionary.txt'
    """
    with open('dictionary.txt', mode='r') as dictionary:
        dictionary_data = dictionary.readlines()
        random_number = random.randrange(0, len(dictionary_data))
        word = dictionary_data[random_number].replace('\n', '')

    return word

def hide_word(word):
    """
    Return a string of '*' with en length equivalent to 'word'
    """
    word_length = len(word)
    hidden_word = str()
    while word_length > 0:
        hidden_word += '*'
        word_length -= 1

    return hidden_word

def game(lives, hanging_tree, word, hidden_word):
    """
    The core function for play to the game
    """
    letters_played = list()
    word = list(word)
    hidden_word = list(hidden_word)

    while lives > 0 and hidden_word != word:
        # We ask the player a letter
        try:
            print('\nThe word to find is: {}'.format(''.join(hidden_word)))
            player_letter = input('==> Type a letter: ')
            player_letter = player_letter[0].upper()
            assert player_letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        except AssertionError:
            print('Please type a correct letter.')
            continue

        # We check the player have not already give this letter
        if player_letter in letters_played:
            print('You already give this letter.')
            continue
        else:
            letters_played.append(player_letter)

        # We check if the letter is in the word to find
        find_letter = False
        for i, letter in enumerate(word):
            if letter == player_letter:
                hidden_word[i] = player_letter
                find_letter = True

        # We check if the player found a letter
        if find_letter:
            print('Yes, "{}" is in the word.'.format(player_letter))
        else:
            lives -= 1
            print('No, "{}" is not in the word'.format(player_letter))
            display_tree(hanging_tree, lives)

    # We check if the word is completly found by the gamer
    if hidden_word == word:
        print('\nCongratulation! You found the word "{}"'.format(''.join(word)))
    else:
        print('\nYou loose!')
        print('The word was: {}'.format(''.join(word)))

    return lives

def display_tree(hanging_tree, lives):
    """
    Draw an hanging tree each time the player give a wrong letter
    """

    for line in hanging_tree[lives]:
        print(line)

def continue_menu():
    """
    A menu to ask the player if she/he wants to continue the game
    """
    player_answer = ''

    while player_answer == '':
        try:
            player_answer = input('\n\n==> Do you want to continue to play? [Y/N] ')
            player_answer = player_answer.upper()

            assert player_answer in ('YES', 'NO', 'Y', 'N')
        except AssertionError:
            print('Please type a correct answer')
            player_answer = ''
            continue

    if player_answer in ('YES', 'Y'):
        print('\nLet\'s gor for an other game!')
        game_continue = True
    else:
        print('\nOoooh. See you another time!')
        game_continue = False

    return game_continue

if __name__ == '__main__':
    print('Access denied.')
