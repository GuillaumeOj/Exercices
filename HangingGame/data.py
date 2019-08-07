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
    
    """
    The hanging tree complete scheme
        _________
        | /    |
        |/     |
        |      O
        |     /|\
        |     / \
     ___|______
    """
    hanging_tree = [
        ['___|______'],
        ['___|______', '|', '|', '|', '|', '|'],
        ['___|______', '|', '|', '|', '|/', '| /'],
        ['___|______', '|', '|', '|', '|/', '| /', '_________'],
        ['___|______', '|', '|', '|', '|/     |', '| /    |', '_________'],
        ['___|______', '|', '|', '|      O', '|/     |', '| /    |', '_________'],
        ['___|______', '|', '|     /|\\', '|      O', '|/     |', '| /    |', '_________'],
        ['___|______', '|     / \\', '|     /|\\', '|      O', '|/     |', '| /    |', '_________']]

    return life, hanging_tree

if __name__ == '__main__':
    print('Access denied.')
