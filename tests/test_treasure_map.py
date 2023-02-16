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


if __name__ == "__main__":
    unittest.main()
