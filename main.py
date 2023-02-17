"""
Fichier d'entrée pour tester le programme
Peut prendre des paramètres en entrée

Utilisation: python treasuremap/main.py [-f file] [-d delay]
"""
import time
import sys
import os
from treasuremap.treasure_map import TreasureMap

if __name__ == "__main__":
    OUTPUT_FILE_NAME = "output.txt"
    DELAY = 0.5

    if len(sys.argv) != 1:
        if "-d" in sys.argv:
            opt_index = sys.argv.index("-d")
            if len(sys.argv) <= opt_index + 1:
                print(
                    "Utilisation: python treasuremap/main.py [-f file] [-d delay]")
                exit(1)
            try:
                DELAY = float(sys.argv[opt_index + 1])
            except ValueError:
                print(
                    "Utilisation: python treasuremap/main.py [-f file] [-d delay]")
                exit(1)
        if "-f" in sys.argv:
            opt_index = sys.argv.index("-f")
            if len(sys.argv) <= opt_index + 1:
                print(
                    "Utilisation: python treasuremap/main.py [-f file] [-d delay]")
                exit(1)
            OUTPUT_FILE_NAME = sys.argv[opt_index + 1]

    INPUT_DESCRIPTION = """C - 3 - 4
M - 1 - 0
M - 2 - 1
T - 0 - 3 - 2
T - 1 - 3 - 3
A - Lara - 1 - 1 - S - AADADAGGA
"""
    tmap = TreasureMap(INPUT_DESCRIPTION)
    i = 1
    print("Initial state : ")
    print(tmap)
    print("1er tour:")
    while tmap.do_turn(verbose=True):
        time.sleep(DELAY)
        i += 1
        print(f"{i}e tour:")

    with open(os.path.join(os.getcwd(), OUTPUT_FILE_NAME), "w", encoding="utf-8") as file:
        file.write(tmap.get_definition())
