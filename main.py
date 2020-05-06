# coding: utf-8
import os

array = [[' '] * 3 for i in range(0,3)]

print(array[0])
print(array[1])
print(array[2])

CoordsX = 0
CoordsY = 0

def afficherTab():
    print(array[0])
    print(array[1])
    print(array[2])
    print("\n\n")

remplie = 0
    
def gagne(joueur):
        win = False
        global remplie
        #Teste les lignes
        for ligne in range (1,len(array)+1):
            if (array[CoordsX][0]==array[CoordsX][1] and array[CoordsX][1]==array[CoordsX][2] and array[CoordsX][1]!=" "):
                victoire=joueur
        #Teste les colonnes
        for col in range (1,len(array)+1):
            if (array[0][CoordsY]==array[1][CoordsY] and array[1][CoordsY]==array[2][CoordsY] and array[1][CoordsY]!=" "):
                victoire=joueur
        #Teste deux diagonales
        rang=1
        if (array[rang][rang]==array[rang+1][rang+1] and array[rang+1][rang+1]==array[rang+2][rang+2] and array[rang+1][rang+1]!=" "):
            victoire=joueur
        if (array[rang+2][rang]==array[rang+1][rang+1] and array[rang+1][rang+1]==array[rang][rang+2] and array[rang+1][rang+1]!=" "):
            victoire=joueur
        #Un gagnant ?
        if victoire!=0:
            print("le joueur %s gagne"%[victory])
            exit()
        #Match nul ?
        if remplie==dimensions*dimensions:
            print("match nul")
            exit()
    
def saisieCoords(joueur):
    
    if joueur == 1:
         
        CoordsX = int(input("Choisissez la case en x : "))
        CoordsY = int(input("Choisissez la case en y : "))
        
        
        while array[CoordsY-1][CoordsX-1] != ' ' :
            print("La case a déja été choisie ! Choisissez une autre position")
            CoordsX = int(input("Choisissez la case en x : "))
            CoordsY = int(input("Choisissez la case en y : "))
            
        print("Le joueur " + str(joueur) + " a joué !")
        array[CoordsY-1][CoordsX-1] = 'x'
        
        gagne(1)
        
    elif joueur == 2:
        
        CoordsX = int(input("Choisissez la case en x : "))
        CoordsY = int(input("Choisissez la case en y : "))    
        
        
        while array[CoordsY-1][CoordsX-1] != ' ' :
            print("La case a déja été choisie ! Choisissez une autre position")
            CoordsX = int(input("Choisissez la case en x : "))
            CoordsY = int(input("Choisissez la case en y : "))
        
        print("Le joueur " + str(joueur) + " a joué !")
        array[CoordsY-1][CoordsX-1] = 'o'
        
        gagne(2)
        
win = False 
joueur = 1

while win == False:
    if joueur == 1:
        print("C'est au joueur 1 de jouer !")
        saisieCoords(1)
        afficherTab()
        joueur = 2
    elif joueur == 2:
        print("C'est au joueur 2 de jouer !")
        saisieCoords(2)
        afficherTab()
        joueur = 1
        
    
    
os.system("pause")