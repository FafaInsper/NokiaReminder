import pygame
from pygame.locals import *
from sys import exit

pygame.init() #Iniciando funções do pygame

larguratela = 700
alturatela = 700
nome = "Nokia Reminder"

tela = pygame.display.set_mode((larguratela, alturatela))
pygame.display.set_caption(nome)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
