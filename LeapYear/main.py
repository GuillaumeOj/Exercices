# -*- coding: utf-8 -*-
"""
Author: GuillaumeOj

Context: OpenClassrooms course
https://openclassrooms.com/fr/courses/235344-apprenez-a-programmer-en-python

Version: 2019.07

This program tell user if a year is a leap year
"""

def main():
    """
    Main function for interact with the user
    """

    year_confirmation = False

    while year_confirmation is not True:
        try:
            # Asking user for a year
            year = input("Give me a year: ")
            year = int(year)

            # This programm don't work for negative years
            assert year >= 0
        except ValueError:
            print("Please give me a correct year !")
        except AssertionError:
            print("Please give me a year greater than or equal to zero.")
        else:
            year_confirmation = True
            testing_year(year)

def testing_year(year):
    """
    Function for testing if a year is a leap year
    """

    # Testing if the 'year' is a leap year
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        message = "is a leap year."
    else:
        message = "is not a leap year."

    print(year, message)


if __name__ == '__main__':
    main()
