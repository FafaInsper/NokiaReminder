import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init() #Iniciando funções do pygame

larguratela = 700
alturatela = 700
nome = "Nokia Reminder"
x = larguratela/2
y = alturatela/2

x_azul = randint(50, 650)
y_azul = randint(60, 640)

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

    ret_vermleho = pygame.draw.rect(tela, (255,0,0), (x,y,50,60)) 
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 50, 60))
   
    if ret_vermleho.colliderect(ret_azul):
        x_azul = randint(50, 650)
        y_azul = randint(60, 640)

    pygame.display.update()