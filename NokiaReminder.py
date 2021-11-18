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

fonte = pygame.font.SysFont('comic sans', 40, True, False)
pontos = 0

tela = pygame.display.set_mode((larguratela, alturatela))
pygame.display.set_caption(nome)
clock = pygame.time.Clock()

while True:
    clock.tick(280)
    tela.fill((0, 0, 0))

    mensagem = f'Pontos: {pontos}'
    textofinal = fonte.render(mensagem, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                x = x - 5
            if event.key == K_d:
                x = x + 5
            if event.key == K_w:
                y = y - 5
            if event.key == K_s:
                y = y + 5

    if pygame.key.get_pressed()[K_a]:
        x = x - 5
    if pygame.key.get_pressed()[K_d]:
        x = x + 5    
    if pygame.key.get_pressed()[K_w]:
        y = y - 5
    if pygame.key.get_pressed()[K_s]:
        y = y + 5 

    ret_vermleho = pygame.draw.rect(tela, (255,0,0), (x,y,50,60)) 
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 50, 60))
   
    if ret_vermleho.colliderect(ret_azul):
        x_azul = randint(50, 650)
        y_azul = randint(60, 640)
        pontos = pontos + 1

    tela.blit(textofinal, (450, 40))

    pygame.display.update()