"""
Fichier de test couvrant treasuremap/treasure_map.py
"""

import unittest
import os
from treasuremap.treasure_map import TreasureMap
from treasuremap.adventurer import Adventurer


class TreasureMapTests(unittest.TestCase):
    """
    Classe de test pour la classe TreasureMap (treasuremap.treasure_map.TreasureMap)
    """

    resource_directory_path = os.path.join(os.getcwd(), "tests", "resource")

    def test_definition(self):
        """
        Teste que l'on récupère une definition valable sans faire bouger l'aventurier
        """
        adventurer_data = "A - Lara - 1 - 1 - S - AADADAGGA"
        adventurer_final_definition = "A - Lara - 1 - 1 - S - 0"
        adventurer = Adventurer(adventurer_data)
        self.assertEqual(adventurer.get_description(
        ), adventurer_final_definition, "La définition de l'aventurier n'est pas bonne")

    def test_move(self):
        """
        Teste que l'on arrive a faire bouger l'aventurier dans une carte simple
        """
        adventurer_data = "A - Lara - 0 - 0 - S - AGADDA"
        map_data = """C - 2 - 2
        M - 1 - 1"""
        tmap = TreasureMap(map_data)
        adventurer = Adventurer(adventurer_data)
        while adventurer.do_move(tmap.mountains, [], (2, 2)):
            pass
        self.assertEqual(adventurer.get_description(),
                         "A - Lara - 0 - 1 - W - 0")

    def test_treasure(self):
        """
        Teste que l'on arrive a prendre un tresor
        """
        map_data = """C - 1 - 2
        T - 0 - 1 - 1
        A - Lara - 0 - 0 - S - A"""
        tmap = TreasureMap(map_data)
        tmap.do_turn()

        self.assertEqual(len(tmap.treasures), 0)
        self.assertEqual(tmap.adventurers[0].treasure_nb, 1)

    def test_treasures_multiple(self):
        """
        Teste que l'on arrive a prendre un tresor parmis plusieurs trésors
        """
        map_data = """C - 1 - 2
        T - 0 - 1 - 2
        A - Lara - 0 - 0 - S - A"""
        tmap = TreasureMap(map_data)
        tmap.do_turn()

        self.assertEqual(len(tmap.treasures), 1)
        self.assertEqual(tmap.treasures[0][2], 1)
        self.assertEqual(tmap.adventurers[0].treasure_nb, 1)

    def test_pickup_treasure_without_moving(self):
        """
        Teste que l'on ne prend pas plusieurs trésors sans revenir sur la case
        """
        map_data = """C - 1 - 2
        T - 0 - 1 - 2
        A - Lara - 0 - 0 - S - AGA"""
        tmap = TreasureMap(map_data)
        while tmap.do_turn():
            pass

        self.assertEqual(len(tmap.treasures), 1)
        self.assertEqual(tmap.treasures[0][2], 1)
        self.assertEqual(tmap.adventurers[0].treasure_nb, 1)

    def test_pickup_treasure_n_times(self):
        """
        Teste que l'on peut prendre un tresor en 2 fois
        """
        map_data = """C - 1 - 2
        T - 0 - 1 - 2
        A - Lara - 0 - 0 - S - AGGAGGA"""
        tmap = TreasureMap(map_data)
        while tmap.do_turn():
            pass

        self.assertEqual(len(tmap.treasures), 0)
        self.assertEqual(tmap.adventurers[0].treasure_nb, 2)


if __name__ == "__main__":
    unittest.main()
