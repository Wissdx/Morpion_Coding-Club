# coding: utf-8
import os

array = ["","","","","","","","",""]

print(array)


def saisieCoords(joueur):
    CoordsX = input("Choisissez la case en x : ")
    CoordsY = input("Choisissez la case en y : ")
    
    if joueur == 1:
        print("Joueur 1 à toi de jouer !")
        array[CoordsX] = "x"
        array[CoordsY] = "x"
    elif joueur == 2:
        print("Joueur 2 à toi de jouer !")
        array[CoordsX] = "o"
        array[CoordsY] = "o"
    

continuer = 1
joueur = 1

while continuer == 1:
    if joueur == 1:
        print("C'est au joueur 1 de jouer !")
        saisieCoords(1)
        print(grille)
        joueur = 2
    elif joueur == 2:
        print("C'est au joueur 2 de jouer !")
        saisieCoords(2)
        print(grille)

os.system("pause")