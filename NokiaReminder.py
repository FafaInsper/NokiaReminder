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
    pygame.draw.rect(tela, (255,0,0), (300,400,50,60)) 
    pygame.draw.circle(tela, (0,180,0), (350,290), 45)
    pygame.draw.line(tela, (255,215,0), (370,0), (370,600), 6)

    pygame.display.update()
