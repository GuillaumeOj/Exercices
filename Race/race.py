# -*- coding:utf-8 -*-
"""
On veut faire une course sur un parcours aléatoirement construit et des participants aléatoires.
Pour cela on va faire deux classes TrackPart et Track pour modéliser une piste hétérogène et deux
classes Pilot et Car pour faire un combo participant de course.

Voici les attributs et méthodes des classes à faire.

Class TrackPart, liste des attributs:
- length: Un entier entre 0 et 10
- terrain: Un des 4 choix suivants "asphalt", "sand", "mud", "rocky"
- complexity: Un des 3 choix suivants "normal", "rapid", "subtle"

Class Track, liste des attributs:
- parts: Liste de TrackParts (par défaut on en génère 20)

Class Pilot, liste des attributs:
- name: Une lettre majuscule
- normal_speed: Un nombre flottant entre 0.5 et 1.5
- rapid_speed: Un nombre flottant entre 0.5 et 1.5
- subtle_speed: Un nombre flottant entre 0.5 et 1.5

Class Car, liste des attributs:
- name: Un numéro entre 1 et 20
- pilot: Un pilote (on peut le générer à la volée)
- asphalt_speed: Un nombre flottant entre 0.5 et 1.5
- sand_speed: Un nombre flottant entre 0.5 et 1.5
- mud_speed: Un nombre flottant entre 0.5 et 1.5
- rocky_speed: Un nombre flottant entre 0.5 et 1.5
Et il faut aussi faire les méthodes d'instance suivantes:
- time_for_part: prends comme argument un TrackPart et donne le temps pour la voiture/pilote sur le
             tronçon il faut prendre en compte le terrain (et vitesse de voiture sur ce terrain)
             et aussi la complexité (et la vitesse de pilote pour ce genre de complexité)
             on multiplie les vitesses (en partant d'une vitesse de 1) avec la longueur du tronçon
- time_for_track: prends comme argument un Track et utilise time_for_part sur les différents
             tronçons renvoie le temps total sur la piste

Faire un print pour chacun des éléments suivants
1) Générer une piste avec 20 tronçons
2) Générer 5 voitures avec pilotes
3) Calculer les temps pour chaque voiture sur la piste
4) Indiquer le vainqueur

En lançant le script on devrait avoir un affichage du genre qui suit:
Using track: rapid sand (3) + subtle rocky (4) + rapid asphalt (6) + rapid asphalt (9) +
     subtle rocky (9) + normal rocky (8) + rapid mud (4) + rapid sand (6) + subtle rocky (9) +
     normal rocky (6) + normal asphalt (3) + subtle asphalt (6) + rapid rocky (4) +
     rapid asphalt (6) + rapid rocky (4) + normal asphalt (7) + subtle rocky (8) +
     normal sand (6) + normal rocky (7) + subtle asphalt (8)
With cars: Car 9 with Pilot G, Car 20 with Pilot G, Car 4 with Pilot N, Car 4 with Pilot W,
     Car 4 with Pilot B
The times are: [[96.73751345520175, Car 9 with Pilot G], [92.91817878332827, Car 20 with Pilot G],
    [102.3473766304071, Car 4 with Pilot N],
    [148.79336249531696, Car 4 with Pilot W],
    [139.66958580936762, Car 4 with Pilot B]]
THE WINNER IS Car 20 with Pilot G

IMPORTANT: essayer de faire un commit git pour l'ajout de chaque Classe (avec sa méthode __init__)
et un commit par méthode de classe / méthode d'instance.
On devrait donc avoir minimum 6-8 commits, une douzaine de commits est correct mais une vingtaine
ferait un peu beaucoup (à moins que ce soit pour rajouter des améliorations hors-sujet).

Voici le début du programme pour se lancer:
"""

from string import ascii_uppercase
from random import random, randint, choice as randchoice, uniform


class TrackPart:
    """
    This class help to create parts of a track
    """

    MIN_LENGTH = 0
    MAX_LENGTH = 10
    TERRAINS = ["asphalt", "sand", "mud", "rocky"]
    COMPLEXITIES = ["normal", "rapid", "subtle"]

    def __init__(self):
        """
        When a trackpart object is created the 3 parameters were randomly created
        """
        self.length = randint(self.MIN_LENGTH, self.MAX_LENGTH)
        self.terrain = randchoice(self.TERRAINS)
        self.complexity = randchoice(self.COMPLEXITIES)


class Track:
    """
    Tis class create a Track object composed of TrackParts
    By default, a Track is made of 20 TrackParts
    """

    TRACKPARTS_NUMBER = 20

    def __init__(self):
        """
        Initialize Track with two atributes:
            - The default number of trackparts
            - An empty list of trackparts
        """
        self._trackparts_number = self.TRACKPARTS_NUMBER
        self.trackparts_list = list()

    def generate_track(self):
        """
        Generate a track with 'trackparts_number'
        """

        i = self._trackparts_number

        while i > 0:
            self.trackparts_list.append(TrackPart())
            i -= 1

    def print_track(self):
        """
        Print the track
        """
        self.track_message = str()
        for self.trackparts in self.trackparts_list:
            if self.track_message == '':
                self.track_message = 'Using track: '
            else:
                self.track_message += '+ '
            self.track_message += self.trackparts.complexity + ' '
            self.track_message += self.trackparts.terrain + ' '
            self.track_message += '(' + str(self.trackparts.length) + ') '

        print(self.track_message)


class Pilot:
    """
    Create a pilot with:
        - A name
        - A speed for 'normal' trackparts
        - A speed for 'rapid' trackparts
        - A speed for 'subtle' trackparts
    """

    LETTERS = ascii_uppercase

    def __init__(self):
        """
        Initialize each attributes for Pilot
        """
        self.name = randchoice(self.LETTERS)
        self.normal_speed = randint(5, 15) /10
        self.rapid_speed = randint(5, 15) /10
        self.subtle_speed = randint(5, 15) /10


class Car:
    """
    Create a car wit:
        - A name
        - A pilot generated with the class Pilot()
        - A speed for 'asphalt' trackparts
        - A speed for 'sand' trackparts
        - A speed for 'mud' trackparts
        - A speed for 'rocky' trackparts
    """

    def __init__(self):
        """
        Initialize each attributes for Car
        """
        self.name = randint(1, 20)
        self.pilot = Pilot()
        self.asphalt_speed = randint(5, 15) /10
        self.sand_speed = randint(5, 15) /10
        self.mud_speed = randint(5, 15) /10
        self.rocky_speed = randint(5, 15) /10

    def time_for_part(self, trackpart):
        """
        Calculate the time for the car on each trackpart
        """
        # Speed depend on trakcpart terrain
        if trackpart.terrain == 'asphalt':
            self.terrain_speed = self.asphalt_speed
        elif trackpart.terrain == 'sand':
            self.terrain_speed = self.sand_speed
        elif trackpart.terrain == 'mud':
            self.terrain_speed = self.mud_speed
        elif trackpart.terrain == 'rocky':
            self.terrain_speed = self.rocky_speed
        else:
            raise ValueError('The terrain type does\'nt exist!' )

        # Speed depend on trackpart complexity
        if trackpart.complexity == 'normal':
            self.pilot_speed = self.pilot.normal_speed
        elif trackpart.complexity == 'rapid':
            self.pilot_speed = self.pilot.rapid_speed
        elif trackpart.complexity == 'subtle':
            self.pilot_speed = self.pilot.subtle_speed
        else:
            raise ValueError('The complexity type does\'nt exist!' )

        # Time for accomplish the part
        self.time_part = self.terrain_speed * self.pilot_speed * trackpart.length

        print(self.time_part)


def main():
    """
    In this main function, we print out all the results
    """

    # Create and print the track
    track = Track()
    track.generate_track()
    track.print_track()

if __name__ == '__main__':
    main()
