import pygame
from pygame.locals import *
from sys import exit
 
pygame.init() #Iniciando funções do pygame
 
larguratela = 700
alturatela = 700
nome = "Nokia Reminder"
x = larguratela/2
y = alturatela/2
 
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
        ...

        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 35
            if event.key == K_d:
                x = x + 35
            if event.key == K_w:
                y = y - 35
            if event.key == K_s:
                y = y + 35

        if pygame.key.get_pressed()[K_a]:
            x = x - 35
        if pygame.key.get_pressed()[K_d]:
            x = x + 35    
        if pygame.key.get_pressed()[K_w]:
            y = y - 35
        if pygame.key.get_pressed()[K_s]:
            y = y + 35 
   
   
    pygame.draw.rect(tela, (255,0,0), (x,y,50,60))
 
    
 
    pygame.display.update

    