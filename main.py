import pygame
from random import shuffle

#Estáticos
pecas = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[2,2],[2,3],[2,4],[2,5],[2,6],[3,3],[3,4],[3,5],[3,6],[4,4],[4,5],[4,6],[5,5],[5,6],[6,6]]
size = width, height = 1080, 640
white = [255,255,255]
black = [0,0,0]
margemS = 60
margemE = 60
tam = 40
jogadores = [[],[],[],[]]
campo = []*24
jogado = []

for i in range(24):
    campo[i] = []*12

def distribuirPecas():
    embaralhado = list(pecas)
    shuffle(embaralhado)
    for i in range(4):
        jogadores[i] = embaralhado[i*6:(i+1)*6]
    print(jogadores)

def desenharCampo():
    screen = pygame.display.set_mode(size)
    screen.fill(white)
    pygame.draw.rect(screen, black, (margemE, margemS, 960, 480), 5)
    for i in range(1, 24):
        pygame.draw.lines(screen, black, False, [(tam * i + margemE, margemS), (tam * i + margemE, margemS + 40 * 12)], 1)
    for i in range(1, 12):
        pygame.draw.lines(screen, black, False, [(margemE, tam * i + margemS), (margemE + 40 * 24, tam * i + margemS)], 1)

def main():
    pygame.init()
    screen = desenharCampo()
    distribuirPecas()

    while True:
        pygame.mouse.get_pressed()
        pygame.display.update()

main()



