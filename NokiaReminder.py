import pygame
from pygame.locals import *
from sys import exit
 
pygame.init() #Iniciando funções do pygame
 
larguratela = 700
alturatela = 700
nome = "Nokia Reminder"
x = larguratela/2
y = 0
 
tela = pygame.display.set_mode((larguratela, alturatela))
pygame.display.set_caption(nome)
 
clock = pygame.time.Clock()
 
while True:
    clock.tick(280)
    tela.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
 
    pygame.draw.rect(tela, (255,0,0), (x,y,50,60))
 
    if y >= alturatela:
        y = 0
 
    y = y + 1
 
    pygame.display.update