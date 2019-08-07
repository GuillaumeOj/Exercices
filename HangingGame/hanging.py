# -*- coding:utf-8 -*-
"""
Author : GuillaumeOj
Version : 2019-08
Source : https://bit.ly/2OFDxLc


Welcome to my first Hanging game

Here is how it works:
1. The player give her/his name:
    a. The player already exist, she/he starts with her/his former score
    b. The player is new, we create her/his profile in 'scores' file
2. The player has to find the world selected by the game:
    a. 8 life by game
    b. The final is the old one + life saved durign the game
"""
import functions
import data

def main():
    """
    Here is the core of the game
    """

    game_continue = True

    while game_continue:
        print('=== Welcome to the Hanging Game ! ===')
        print('\n')

        # Creating the player
        pseudo, score = functions.register_gamer()

        print('Welcome {}! For now, you score is {}.'.format(pseudo, score))
        print('Let\'s begin the game!')
        print('=====================================')

        # Get the game configuration
        life_configuration, hanging_tree = data.game_configuration()
        life = int(life_configuration)

if __name__ == '__main__':
    main()
