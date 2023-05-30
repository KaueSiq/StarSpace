import pygame
from  tkinter import simpledialog

pygame.init()
tamanho = (960,700)
branco = (255,255,255)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Star Link")
fundo = pygame.image.load("fundo.jpg")
icone = pygame.image.load("space.png")
pygame.display.set_icon(icone)
running = True
estrelas= {}
localizacao = {}
tela.fill(branco)
tela.blit(fundo, (0,0))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False
        elif event.type ==  pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            item = simpledialog.askstring("space ", "Nome da Estrela:")
            pygame.draw.circle (tela, branco, (pos),5)
            print (item)
            if item == None:
                item = "desconhecido"+str (pos)
            estrelas[item] = pos
            print (estrelas)





    
    


    pygame.display.update()

    

pygame.quit()