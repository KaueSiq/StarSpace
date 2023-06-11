from multiprocessing.sharedctypes import Value
import pygame
from  tkinter import simpledialog
from funcoes import historico

pygame.init()
tamanho = (960,700)
branco = (255,255,255)
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("contador Link")
fundo = pygame.image.load("fundo.jpg")
icone = pygame.image.load("space.png")
pygame.display.set_icon(icone)
running = True

fonte = pygame.font.SysFont('Candara',25)

contador = 0
estrelas = {}
cordenadas = []
circulos = []



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
            cordenadas.append((pos),) 
            item = simpledialog.askstring("space ", "Nome da Estrela:")
            if item == '' or item == None:
                item = "desconhecido" + str(pos)
            ponto = pygame.draw.circle (tela, branco, (pos),5)
            contador = contador +1
            if contador > 1:
                linha = pygame.draw.line(tela,branco, cordenadas[-1] , cordenadas[-2],3)
            if event.type ==  pygame.MOUSEBUTTONUP:
                texto = fonte.render(item,True,branco,)
                tela.blit (texto,cordenadas[-1])
                estrelas[item] = pos
                print(estrelas)
            historico(item,pos)
    
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F12:   
                    with open("historico.txt", "w") as arquivo:
                        arquivo.truncate(0)
                        tela.blit(fundo,(0,0))
                        print("conteudo apagado")
                        

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:
                    for key, value in estrelas.items():
                        pygame.draw.circle(tela,branco,value, 5)
                        pygame.draw.line(tela, branco,cordenadas[-1] , cordenadas[-2],3)
                    print ("historico carregado")
                
            
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F10:
                        print ("historico salvo")


    opcao1 = fonte.render("Pressione F10 para salvar o processo atual",True, branco)
    opcao2 = fonte.render("Pressione F11 para carregar o processo antigo", True, branco)           
    opcao3 = fonte.render("Pressione F12 para deletar o processo atual", True, branco) 

    tela.blit(opcao1,(10,10))
    tela.blit(opcao2,(10,35))
    tela.blit(opcao3,(10,60))

    pygame.display.update()

    

pygame.quit()