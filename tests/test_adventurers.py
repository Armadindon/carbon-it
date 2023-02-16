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


if __name__ == "__main__":
    unittest.main()
