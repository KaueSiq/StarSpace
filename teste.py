import pygame
import tkinter as tk
from tkinter import simpledialog

# Inicialização do Pygame
pygame.init()

# Definição das dimensões da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Definição das cores
cor_fundo = (0, 0, 0)
cor_marcação = (255, 255, 255)
cor_linha = (255, 0, 0)

# Variáveis para armazenar as marcações e linhas
marcacoes = []
linhas = []

# Função para abrir uma caixa de diálogo e obter o nome da estrela
def obter_nome_estrela():
    root = tk.Tk()
    root.withdraw()
    nome_estrela = simpledialog.askstring("Nome da Estrela", "Digite o nome da estrela:")
    return nome_estrela

# Função para salvar as marcações em um arquivo
def salvar_marcacoes():
    with open("marcacoes.txt", "w") as arquivo:
        for marcacao in marcacoes:
            arquivo.write(f"{marcacao[0]},{marcacao[1]},{marcacao[2]}\n")

# Função para carregar as marcações de um arquivo
def carregar_marcacoes():
    marcacoes.clear()
    linhas.clear()
    with open("marcacoes.txt", "r") as arquivo:
        for linha in arquivo:
            x, y, nome_estrela = linha.strip().split(",")
            marcacoes.append((int(x), int(y), nome_estrela))

# Função para excluir todas as marcações
def excluir_marcacoes():
    marcacoes.clear()
    linhas.clear()

# Loop principal do jogo
executando = True
clock = pygame.time.Clock()

while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            # Salvar as marcações antes de fechar o programa
            salvar_marcacoes()
            executando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Obter a posição do clique do mouse
            pos_mouse = pygame.mouse.get_pos()
            x, y = pos_mouse
            
            # Obter o nome da estrela
            nome_estrela = obter_nome_estrela()
            
            # Adicionar a marcação à lista de marcações
            marcacoes.append((x, y, nome_estrela))
            
            # Criar linhas entre as marcações
            if len(marcacoes) > 1:
                p1 = marcacoes[-2][:2]
                p2 = marcacoes[-1][:2]
                linhas.append((p1, p2))
    
    # Limpar a tela
    tela.fill(cor_fundo)
    
    # Desenhar as linhas na tela
    for linha in linhas:
        p1, p2 = linha
        pygame.draw.line(tela, cor_linha, p1, p2)
    
    # Desenhar as marcações na tela
    for marcacao in marcacoes:
        x, y, nome_estrela = marcacao
        pygame.draw.circle(tela, cor_marcação, (x, y), 5)
        texto = pygame.font.SysFont(None, 20).render(nome_estrela, True, cor_marcação)
        tela.blit(texto, (x + 10, y - 10))
    
    # Atualizar a tela
        pygame.display.flip()

pygame.quit()

