# -*- coding:utf-8 -*-
"""
All functions used for the hanging game are here
"""
import pickle

def register_gamer():
    """
    Read the scores file.
    If the gamer is not register yet, we create her/his profile
    Else we retrieved gamer's informations (pseudo and score)
    """

    pseudo = input('Please type your pseudo: ')

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

if __name__ == '__main__':
    print('Access denied.')