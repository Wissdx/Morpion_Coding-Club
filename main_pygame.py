# coding: utf-8
import pygame, sys
from pygame.locals import *

# Définition des variables
icone = pygame.image.load("siphano.ico")
rond = pygame.image.load("rond.png")
croix = pygame.image.load("croix.png")

# Initialisation de la fenetre
pygame.init()
pygame.display.set_caption("Morpion")
pygame.display.set_icon(icone)

fenetre = pygame.display.set_mode((600,700))



while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()