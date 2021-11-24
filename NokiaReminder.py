import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init() #Iniciando funções do pygame

pygame.mixer.music.set_volume(0.2)
musica_de_fundo = pygame.mixer.music.load('BoxCat Games - Nameless_ the Hackers Title Screen.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_1-up.wav')
barulho_colisao.set_volume(1)

larguratela = 700
alturatela = 700
nome = "Nokia Reminder"
x_cobra = int(larguratela/2)
y_cobra = int(alturatela/2)

velocidade = 1
x_controle = velocidade
y_controle = 0


x_maca = randint(50, 650)
y_maca = randint(60, 640)

fonte = pygame.font.SysFont('comic sans', 40, True, False)
pontos = 0

tela = pygame.display.set_mode((larguratela, alturatela))
pygame.display.set_caption(nome)
clock = pygame.time.Clock()

lista_cobra = []
comprimento_inicial = 5
morte = False


def aumento_cobra(lista_cobra):
    for xey in lista_cobra:
        #xey = [x, y]
        pygame.draw.rect(tela, (0, 255, 0), (xey[0], xey[1], 20, 20))


while True:
    clock.tick(280)
    tela.fill((255, 255, 255))

    mensagem = f'Pontos: {pontos}'
    textofinal = fonte.render(mensagem, True, (0, 0, 0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle

    cobra = pygame.draw.rect(tela, (0,255,0), (x_cobra,y_cobra,30,30)) 
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 30, 30))
   
    if cobra.colliderect(maca):
        x_maca = randint(50, 650)
        y_maca = randint(60, 640)
        velocidade = velocidade + 0.05
        pontos = pontos + 1
        barulho_colisao.play()
        comprimento_inicial = comprimento_inicial + 10

    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)
    lista_cobra.append(lista_cabeca)    

    if lista_cobra.count(lista_cabeca) > 1:
        morte = True
        
    if x_cobra > larguratela:
        morte = True
    if x_cobra < 0:
        morte = True
    if y_cobra > larguratela:
        morte = True
    if y_cobra < 0:
        morte = True

    
    while morte:
        mensagem_morte = f'Game Over! Você fez {pontos} pontos!'
        fontemorte = pygame.font.SysFont('comic sans', 20, True, False)
        textofinalmorte = fontemorte.render(mensagem_morte, True, (0,0,0))
        ret_texto = textofinalmorte.get_rect()
        tela.fill((255, 255, 255))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
        ret_texto.center = (larguratela//2, alturatela//2)
        tela.blit(textofinalmorte, ret_texto)
        pygame.display.update()

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumento_cobra(lista_cobra)

    tela.blit(textofinal, (450, 40))

    pygame.display.update()