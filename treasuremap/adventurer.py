"""
Le module contenant la classe Adventurer et l'enum Headings
On y retrouve la logique lié au mouvement des aventuriers
"""

from enum import Enum


class Heading(Enum):
    """
    Classe représentant les différentes directions que l'un aventurier
    peut regarder
    """
    NORTH = (0, -1)
    EAST = (1, 0)
    SOUTH = (0, 1)
    WEST = (-1, 0)

    def turn_right(self):
        """Retourne la position à laquelle la personne fait face en tournant à droite

        Returns:
            Heading: La position en tournant à droite
        """
        if self == Heading.NORTH:
            return Heading.EAST
        if self == Heading.EAST:
            return Heading.SOUTH
        if self == Heading.SOUTH:
            return Heading.WEST

        return Heading.NORTH

    def turn_left(self):
        """Retourne la position à laquelle la personne fait face en tournant à gauche

        Returns:
            Heading: La position en tournant à gauche
        """
        if self == Heading.NORTH:
            return Heading.WEST
        if self == Heading.WEST:
            return Heading.SOUTH
        if self == Heading.SOUTH:
            return Heading.EAST

        return Heading.NORTH


headings_correspondances = {
    "N": Heading.NORTH,
    "E": Heading.EAST,
    "S": Heading.SOUTH,
    "W": Heading.WEST
}

inverse_headings_correspondances = {
    Heading.NORTH: "N",
    Heading.EAST: "E",
    Heading.SOUTH: "S",
    Heading.WEST: "W"
}


class Adventurer():
    """Une classe représentant un aventurier"""

    def __init__(self, description: str) -> None:
        """Initialise l'aventurier avec sa ligne

        Args:
            description (str): La description de l'aventurier
        """
        self.current_movement = 0
        self.treasure_nb = 0

        _, self.name, self.position_x, self.position_y, unparsed_heading, unparsed_movements = description.strip().split(" - ")
        self.position_x = int(self.position_x)
        self.position_y = int(self.position_y)
        self.heading = headings_correspondances[unparsed_heading]
        self.movements = list(unparsed_movements)

    def do_move(self, obstacles: list, treasures: list, size: tuple) -> bool:
        """Fait en sorte que l'aventurier face un mouvement

        Args:
            obstacles (list): La liste des obstacles (tuples avec (x,y))
            treasures (list): La liste des trésor, même format que dans TreasureMap

        Returns:
            bool: Renvoie s'il reste des mouvement pour l'aventurier
        """
        move = self.movements[self.current_movement]
        if move == "A":
            new_x = self.position_x + self.heading.value[0]
            new_y = self.position_y + self.heading.value[1]
            mountain_ahead = len(
                list(filter(lambda x: x != (new_x, new_y), obstacles))) == 0
            in_the_map = size[0] > new_x >= 0 and size[1] > new_y >= 0
            # Si il n'y a pas d'obstacle devant (montagne / aventurier),
            # et que l'on sort pas de la carte, on avance l'aventurier
            if not mountain_ahead and in_the_map:
                self.position_x = new_x
                self.position_y = new_y
                # On vérifie également s'il y a un trésor
                treasures_at_pos = list(filter(lambda x: (x[1][0], x[1][1]) == (
                    self.position_x, self.position_y), enumerate(treasures)))
                if len(treasures_at_pos) != 0:
                    treasure_index, treasure_infos = treasures_at_pos[0]
                    # On met à jour le compte de trésors
                    treasure_infos[2] -= 1
                    self.treasure_nb += 1
                    # Si il tombe à 0, on supprime l'entrée
                    if treasure_infos[2] == 0:
                        treasures.pop(treasure_index)

        elif move == "D":
            self.heading = self.heading.turn_right()
        elif move == "G":
            self.heading = self.heading.turn_left()

        self.current_movement += 1
        return not self.finished()

    def __str__(self) -> str:
        """Retourne un affichage simple pour les aventuriers

        Returns:
            str: L'affichage de l'aventurier
        """
        return f"""{self.name} : {self.position_x, self.position_y} a {self.treasure_nb} trésors !
Elle regarde vers {self.heading} et en est à son {self.current_movement + 1}e mouvement !
"""

    def get_description(self) -> str:
        """Retourne la description de l'aventurier

        Returns:
            str: La description de l'aventurier
        """
        return " - ".join(["A",
                           self.name,
                           str(self.position_x),
                           str(self.position_y),
                           inverse_headings_correspondances[self.heading],
                           str(self.treasure_nb)
                           ])

    def finished(self) -> bool:
        """Retourne si l'aventurier a encore des mouvements à réaliser

        Returns:
            bool: S'il ne reste pas de mouvements à l'aventurier
        """
        return self.current_movement == len(self.movements)

    def get_short_heading(self) -> str:
        """Retourne la simplification de la direction regardée (N,S,W,E)

        Returns:
            str: La simplification de la direction
        """
        return inverse_headings_correspondances[self.heading]

