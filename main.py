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


star = 0
estrelas= {}
cordenadas= []


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
            cordenadas.append(pos)
            print(cordenadas)   
            item = simpledialog.askstring("space ", "Nome da Estrela:")
            circulo = pygame.draw.circle (tela, branco, (pos),5)
            print (len,cordenadas)           
            #cordenadas[-2]
            if star > 1:
                linha = pygame.draw.line(tela,branco, (cordenadas[0,1]),5)

                #print(star,"erro")
            star = star +1

            
            print (item)
            if item == None:
                item = "desconhecido"+str (pos)
            estrelas[item] = pos
            print()
        





    
    


    pygame.display.update()

    

pygame.quit()