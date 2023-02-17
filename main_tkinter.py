"""
Fichier d'entrée pour tester le programme
Peut prendre des paramètres en entrée

Version Bonus, permet seulement d'avoir un affichage via TKINTER
mais fait la même chose que main.py

Utilisation: python treasuremap/main.py [-f file] [-d delay]
"""
import time
import sys
import os
import re
from tkinter import Tk, Canvas
from treasuremap.treasure_map import TreasureMap


def update_display(drawing_zone: Canvas, square_size=50):
    """Update l'écran tkinter

    Args:
        canvas (_type_): _description_
    """
    drawing_zone.delete("all")
    matrix = tmap.get_matrix()
    for i in range(tmap.height):
        for j in range(tmap.width):
            # On dessine le carré de terre
            drawing_zone.create_rectangle(
                j * square_size,
                i * square_size,
                (j + 1) * square_size,
                (i + 1) * square_size,
                fill="green"
            )

            # Si il y en a une, on dessine une montagne
            if matrix[i][j] == "M":
                drawing_zone.create_polygon([
                    j * square_size + (square_size * 1 / 2),
                    i * square_size + (square_size * 1 / 6),
                    j * square_size + (square_size * 1 / 6),
                    i * square_size + (square_size * 5 / 6),
                    j * square_size + (square_size * 5 / 6),
                    i * square_size + (square_size * 5 / 6),
                ], fill="gray")

            # On affiche le trésor, et le nombre de trésor qu'il y a
            if matrix[i][j].startswith("T"):
                nb_treasure = re.match(r"T\((\d*)\)", matrix[i][j]).group(1)
                drawing_zone.create_oval([
                    j * square_size + (square_size / 2) - (square_size / 2.5),
                    i * square_size + (square_size / 2) - (square_size / 2.5),
                    j * square_size + (square_size / 2) + (square_size / 2.5),
                    i * square_size + (square_size / 2) + (square_size / 2.5),
                ], fill="yellow")
                drawing_zone.create_text(j * square_size + (square_size / 2),
                                         i * square_size + (square_size / 2),
                                         text=nb_treasure, justify='center')

            # On affiche l'aventurier et son orientation
            if matrix[i][j].startswith("A"):
                orientation = re.match(r"A\((.)\)", matrix[i][j]).group(1)
                drawing_zone.create_oval([
                    j * square_size + (square_size * 2/6),
                    i * square_size + (square_size * 5/6),
                    j * square_size + (square_size * 4/6),
                    i * square_size + (square_size * 1/6),
                ], fill="blue")
                drawing_zone.create_text(j * square_size + (square_size / 2),
                                         i * square_size + (square_size / 2),
                                         text=orientation, justify='center')

    drawing_zone.pack()


if __name__ == "__main__":
    OUTPUT_FILE_NAME = "output.txt"
    DELAY = 2

    if len(sys.argv) != 1:
        if "-d" in sys.argv:
            opt_index = sys.argv.index("-d")
            if len(sys.argv) <= opt_index + 1:
                print(
                    "Utilisation: python treasuremap/main.py [-f file] [-d delay]")
                sys.exit(1)
            try:
                DELAY = float(sys.argv[opt_index + 1])
            except ValueError:
                print(
                    "Utilisation: python treasuremap/main.py [-f file] [-d delay]")
                sys.exit(1)
        if "-f" in sys.argv:
            opt_index = sys.argv.index("-f")
            if len(sys.argv) <= opt_index + 1:
                print(
                    "Utilisation: python treasuremap/main.py [-f file] [-d delay]")
                sys.exit(1)
            OUTPUT_FILE_NAME = sys.argv[opt_index + 1]

    INPUT_DESCRIPTION = """C - 3 - 4
M - 1 - 0
M - 2 - 1
T - 0 - 3 - 2
T - 1 - 3 - 3
A - Lara - 1 - 1 - S - AADADAGGA
"""
    tmap = TreasureMap(INPUT_DESCRIPTION)

    # Gestion de l'affichage avec TKINTER
    root = Tk()
    canvas = Canvas(root, width=tmap.width * 50, height=tmap.height * 50)
    update_display(canvas)
    root.update()
    time.sleep(DELAY)
    while tmap.do_turn():
        time.sleep(DELAY)
        update_display(canvas)
        root.update()
    time.sleep(DELAY)

    # Enregistrement du fichier
    with open(os.path.join(os.getcwd(), OUTPUT_FILE_NAME), "w", encoding="utf-8") as file:
        file.write(tmap.get_definition())
