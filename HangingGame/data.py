# -*- coding:utf-8 -*-
"""
This module contains all data needed for the game
"""
def game_configuration():
    """
    All data for the game are return by this function
    'life', 'hanging_tree'
    """

    life = 8

    #The hanging tree complete scheme
    #    ________
    #    | /    |
    #    |/     |
    #    |      O
    #    |     /|\
    #    |     / \
    # ___|______

    hanging_tree = [
        ['   ________',
         '   | /    |',
         '   |/     |',
         '   |      O',
         '   |     /|\\',
         '   |     / \\',
         '___|______'],
        ['   ________',
         '   | /    |',
         '   |/     |',
         '   |      O',
         '   |     /|\\',
         '   |',
         '___|______'],
        ['   ________',
         '   | /    |',
         '   |/     |',
         '   |      O',
         '   |',
         '   |',
         '___|______'],
        ['   ________',
         '   | /    |',
         '   |/     |',
         '   |',
         '   |',
         '   |',
         '___|______'],
        ['   ________',
         '   | /',
         '   |/',
         '   |',
         '   |',
         '   |',
         '___|______'],
        ['   | /',
         '   |/',
         '   |',
         '   |',
         '   |',
         '___|______'],
        ['   |',
         '   |',
         '   |',
         '   |',
         '   |',
         '___|______'],
        ['___|______']]

    return life, hanging_tree

if __name__ == '__main__':
    print('Access denied.')
