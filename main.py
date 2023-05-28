import pygame
from  tkinter import simpledialog

pygame.init()
tamanho = (960,723)
branco = (255,255,255)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Star Link")
running = True
estrelas =[]
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type ==  pygame.MOUSEBUTTONUP:
            pos = pygame .mouse.get_pos()
            item = simpledialog.askstring("space ", "Nome da Estrela:")
            print (item)
            if item == None:
                item = "desconhecido" + str (pos)
            estrelas[item] = pos







    pygame.display.update()

    

pygame.quit()