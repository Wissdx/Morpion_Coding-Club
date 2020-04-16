# coding: utf-8
import os

array = [[''] * 3 for i in range(0,3)]

print(array[0])
print(array[1])
print(array[2])

def saisieCoords(joueur):
    CoordsX = int(input("Choisissez la case en x : "))
    CoordsY = int(input("Choisissez la case en y : "))
    
    if joueur == 1:
        if CoordsX == "x" and CoordsY == "x":
            print("La case a déja été choisie !")
            pass           
        else:
            print("Joueur 1 à toi de jouer !")
            array[CoordsY-1][CoordsX-1] = 'x'
    elif joueur == 2:
        if CoordsX == "o" and CoordsY == "o":
            print("La case a déja été choisie !")
            pass
        else:
            print("Joueur 2 à toi de jouer !")
            array[CoordsY-1][CoordsX-1] = 'o'
    

continuer = 1
joueur = 1

while continuer == 1:
    if joueur == 1:
        print("C'est au joueur 1 de jouer !")
        saisieCoords(1)
        print(array[0])
        print(array[1])
        print(array[2])
        joueur = 2
    elif joueur == 2:
        print("C'est au joueur 2 de jouer !")
        saisieCoords(2)
        print(array[0])
        print(array[1])
        print(array[2])
        joueur = 1
    

os.system("pause")