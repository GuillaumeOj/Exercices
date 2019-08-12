# -*- coding: utf-8 -*-
"""
Author: GuillaumeOj

Context: OpenClassrooms course
https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python

Version: 2019.08

This program is a game for playing roulette. Rules or not exactly the real one
for simplify the program.

Rules:
1. The player bet on a number between 0 and 49
2. Even numbers or black and odd numbers or red.
3. If the number is the one bet by the player, he win 3 time the bet
4. If the number is the same color bet by the player, he win 50% of the bet
"""
from random import randrange
from math import ceil

def main():
    """
    Here is the main part of the program
    It's were the player is gaming
    """

    player_bank = -1
    player_bet = 0
    game = True

    print("============= WELCOME TO ZCASIN0 =============")

    # Roulette asking player how much he wants to play
    while player_bank == -1:
        try:
            player_bank = input("--> How much money do you have? ")
            player_bank = int(player_bank)

            assert player_bank > 0
        except ValueError:
            print("== Please give me a real integer!")
            player_bank = -1
        except AssertionError:
            print("== Please give me number greater than Zer0!")
            player_bank = -1
        else:
            print("----")
            print("OK, you have", player_bank, "$! Let's play!!")
            print("----")

    while player_bank > 0 and game:
        # Player give a number
        player_number = game_number()
        # Player give a bet
        player_bet, player_bank = game_bet(player_bank)

        # Roulette give a number
        roulette_number = game_roulette()
        print("----")
        print("The roulette number is:", roulette_number)

        # The game compare 'player_number' and 'roulette_number'
        player_bank = game_compare(player_number,
                                   roulette_number,
                                   player_bank,
                                   player_bet)
        if player_bank > 0:
            print("You have now", player_bank, "$!")
            game = game_continue()
        else:
            print("You are out of money, sorry you leave the table")

def game_number():
    """
    The player choose a number between 0 and 49
    """
    player_number = -1

    while player_number < 0 or player_number > 49:
        try:
            player_number = input("--> Please give me a number between 0 and 49: ")
            player_number = int(player_number)

            assert player_number in range(0, 49)
        except ValueError:
            print("Please give me a correct number!")
            player_number = -1
        except AssertionError:
            print("Please give me a number between 0 and 49!")
            player_number = -1
        else:
            return player_number

def game_bet(player_bank):
    """
    The player give a bet according his/her bank
    """
    player_bet = -1

    print("---")
    print("You have", player_bank, "$ in your bank")

    while player_bet <= 0:
        try:
            player_bet = input("--> Please give me a bet: ")
            player_bet = int(player_bet)

            assert player_bet >= 1 and player_bet <= player_bank
        except ValueError:
            print("Give me a real integer")
            player_bet = -1
        except AssertionError:
            print("Give me a bet between 1 and", player_bank)
            player_bet = -1
        else:
            player_bank -= player_bet
            return player_bet, player_bank

def game_roulette():
    """
    The roulette give a random number between 0 and 49
    """

    return randrange(0, 49)

def game_compare(player_number, roulette_number, player_bank, player_bet):
    """
    This function compare 'player_number' and 'roulette_number' depending on
    result, it return the new 'player_bank' value
    """

    if roulette_number == player_number:
        bet_result = player_bet * 3

        player_bank += bet_result
        print("Numbers or the same, congratulation, you win", bet_result, "$!")
    elif (player_number % 2) == 0 and (roulette_number % 2) == 0:
        bet_result = ceil(player_bet / 2)

        player_bank += bet_result
        print("Each numbers or black, you win", bet_result, "$!")
    elif (player_number % 2) != 0 and (roulette_number %2) != 0:
        bet_result = ceil(player_bet / 2)

        player_bank += bet_result
        print("Each numbers or red, you win", bet_result, "$!")
    else:
        print("Sorry you lost", player_bet, "$.")

    return player_bank

def game_continue():
    """
    Here the game ask the player if he wants to continue the game
    """
    game = ""

    print("")
    print("----")

    while game == "":
        player_answer = input("Do you want to continue the game? [Y/N] ")
        if player_answer in ("Yes", "YES", "Y", "y", "yes"):
            game = True
        elif player_answer in ("No", "NO", "N", "n", "no"):
            game = False
            print("Oooooh, sorry you want to leave. See you soon !")
        else:
            print("Sorry I did not understand your answer.")

    return game

if __name__ == '__main__':
    main()
