import pygame
from  tkinter import simpledialog
from funcoes import historico , salvar_posicao, conversao , salvar_historico

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
nome_arquivo = 'posicao.txt'  # substitua pelo nome do seu arquivo
tuplas = conversao(nome_arquivo)

# Exemplo de uso:
for tupla in tuplas:
    print(tupla)

historico2 = {
    
}
salvarEstrelas = "historico.txt"
salvar_historico(historico2, salvarEstrelas)

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
                #print(estrelas)
                print(cordenadas)
            historico(item,pos)
            salvar_posicao(pos)
    
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F12:   
                    with open("historico.txt", "w") as arquivo:
                        arquivo.truncate(0)
                    with open("posicao.txt", "w") as arquivo:
                        arquivo.truncate(0)
                        tela.blit(fundo,(0,0))
                        print("conteudo apagado")
                        cordenadas = []
                        #estrelas = {}
                        contador = 0
                        
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F11:      
                    #try:    
                    for key, value in historico2.items():
                            pygame.draw.circle(tela,branco,value, 5)
                            contador = contador + 1
                            print(contador)
                            if contador > 1:
                                for tupla in tuplas:
                                    pygame.draw.line(tela, branco,tuplas[-1],tuplas[-2],3)
                    print ("historico carregado")
                        
                    #except:
                        #print ("voce nn tem um historico salvo")
                        
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