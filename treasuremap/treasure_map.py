"""
Fichier principal du module, contient la classe TreasureMap qui contient
quasiment toute la logique de l'exercice
"""

from treasuremap.adventurer import Adventurer


class TreasureMap():
    """
    Classe principale du projet, elle y contient la structure de données
    de la carte. On y stocke les données sous une forme de plusieurs listes
    mais on peut également récupérer des données sous format matricielle.
    """

    def __init__(self, description: str) -> None:
        """Initialisation de l'objet TreasureMap et construction de la structure

        Args:
            description (str): Le contenu du fichier représentant la carte
        """
        self.width, self.height = 0, 0
        self.mountains = []
        self.treasures = []
        self.adventurers = []

        # On commence par nettoyer l'input
        instructions = list(filter(lambda x: bool(
            x.strip()), description.splitlines()))

        # La première ligne est la taille de la carte
        self.width, self.height = tuple(
            map(int, instructions[0].split("-")[1:]))

        # On itère les lignes suivante pour remplir la structure de données de la carte
        for instruction in instructions[1:]:
            action, *parameters = tuple(
                map(lambda x: x.strip(), instruction.split("-")))

            if action != "A":
                # On convertit les paramètres en entier (sauf dans le cas d'un aventurier)
                parameters = tuple(map(int, parameters))

            # On ajoute dans la bonne liste
            if action == "M":
                self.mountains.append((parameters[0], parameters[1]))
            elif action == "T":
                self.treasures.append(
                    [parameters[0], parameters[1], parameters[2]])
            elif action == "A":
                self.adventurers.append(Adventurer(instruction))

    def get_matrix(self) -> list[list[str]]:
        """Méthode utilitaire afin de renvoyer les données sous forme matricielle

        Returns:
            list[list[str]]: La matrice de string représentant l'état actuel de la carte
        """
        matrix = [["." for j in range(self.width)] for i in range(self.height)]

        # On ajoute le contenu de nos listes
        for m_x, m_y in self.mountains:
            matrix[m_y][m_x] = "M"

        for t_x, t_y, t_n in self.treasures:
            matrix[t_y][t_x] = f"T({t_n})"

        for adv in self.adventurers:
            # On affiche l'aventurier seulement si il n'y a rien d'autre qui occupe la case
            if matrix[adv.position_y][adv.position_x] == ".":
                matrix[adv.position_y][adv.position_x] = f"A({adv.get_short_heading()})"

        return matrix

    def get_definition(self) -> str:
        """Retourne une chaine de caractères représentants le fichier de description de la carte

        Returns:
            str: Contenu du description de la carte
        """
        definition = f"C - {self.width} - {self.height}\n"
        definition += "\n".join(map(lambda x: "M - " +
                                " - ".join(map(str, x)), self.mountains)) + "\n"
        definition += "\n".join(map(lambda x: "T - " +
                                " - ".join(map(str, x)), self.treasures))
        if len(self.adventurers) != 0:
            definition += "\n" + \
                "\n".join(map(lambda x: x.get_description(), self.adventurers))

        return definition

    def __str__(self) -> str:
        """Renvoie une représentation sous chaine de caractère (utilisé pour le debug)

        Returns:
            str: La forme matricielle de la matrice
        """
        matrix = self.get_matrix()
        return '\n'.join(['\t'.join(line) for line in matrix])

    def do_turn(self, verbose=False) -> bool:
        """Réalise un tour de "jeu" en mettant à jour les positions des aventuriers

        Args:
            verbose (bool, optional): Si on affiche la matrice a chaque tour. Désactivé par défaut.

        Returns:
            bool: _description_
        """
        remaining_adventurers = list(
            filter(lambda x: not x.finished(), self.adventurers))
        for adv in remaining_adventurers:
            # On recalcule la position des aventuriers
            # a chaque itération pour gérer les obstacles
            obstacles = self.mountains + \
                list(map(lambda x: (x.position_x, x.position_y), self.adventurers))
            adv.do_move(obstacles, self.treasures,
                        (self.width, self.height))

        if verbose:
            print(self, "\n")

        return not all(map(lambda x: x.finished(), self.adventurers))
