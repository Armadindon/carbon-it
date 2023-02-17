"""
Fichier de test couvrant treasuremap/treasure_map.py
"""

import unittest
import os
from treasuremap.treasure_map import TreasureMap


class TreasureMapTests(unittest.TestCase):
    """
    Classe de test pour la classe TreasureMap (treasuremap.treasure_map.TreasureMap)
    """

    resource_directory_path = os.path.join(os.getcwd(), "tests", "resource")

    def test_definition(self):
        """
        Teste que l'on récupère bien la même description qu'au début 
        avec la méthode TreasureMap::get_definition
        """
        test_file_path = os.path.join(self.resource_directory_path, "map1.txt")
        description = ""
        with open(test_file_path, "r", encoding="utf-8") as file:
            description = file.read()

        tmap = TreasureMap(description)
        self.assertEqual(tmap.get_definition(), description,
                         "On ne retombe pas sur la description initiale")

    def test_matrix(self):
        """
        Teste que l'on récupère une représentation matricielle correcte 
        en faisant la conversion en matrice
        """
        test_file_path = os.path.join(self.resource_directory_path, "map1.txt")
        description = ""
        requested_result = ".\tM\t.\n.\t.\tM\n.\t.\t.\nT(2)\tT(3)\t."
        with open(test_file_path, "r", encoding="utf-8") as file:
            description = file.read()

        tmap = TreasureMap(description)
        self.assertEqual(str(tmap), requested_result,
                         "On ne retombe pas sur la bonne structure")

    def test_full_game(self):
        """
        Teste que l'on arrive a faire une simulation de A à Z
        En prenant l'exemple de l'exercice
        """
        test_file_path = os.path.join(self.resource_directory_path, "map2.txt")
        description = ""
        with open(test_file_path, "r", encoding="utf-8") as file:
            description = file.read()

        tmap = TreasureMap(description)

        while tmap.do_turn():
            pass

        self.assertEqual(
            (tmap.adventurers[0].position_x, tmap.adventurers[0].position_y), (0, 3))
        self.assertEqual(tmap.adventurers[0].name, "Lara")
        self.assertEqual(tmap.adventurers[0].get_short_heading(), "S")
        self.assertEqual(tmap.adventurers[0].treasure_nb, 3)
        self.assertEqual(len(tmap.treasures), 1)
        self.assertEqual(tmap.treasures[0], [1, 3, 2])
        self.assertEqual(len(tmap.mountains), 2)


if __name__ == "__main__":
    unittest.main()
