# La carte au trésor

Exercice réalisé avant un entretien technique auprès de Carbon IT

## Lancement du progamme

On peut lancer le programme depuis la racine du projet avec : `python main.py [-f file] [-d delay]`
Il y a des options supplémentaires:
  - `-d` pour la gestion du delai entre les tours (par défaut: 0.5 secondes)
  - `-f` pour passer le nom / dossier du fichier de sortie (par défaut: output.txt)

Il y a également une version "Bonus" du programme avec un affichage géré par Tkinter `python main_tkinter.py [-f file] [-d delay]`, il vous faut la librairie installé pour l'utiliser (`sudo apt install python3-tk` sur ubuntu).