def historico(item,pos):
    arquivo = open("historico.txt", "a+") 
    arquivo.write (item)
    arquivo.write(",")
    arquivo.write(str(pos))
    palavra = item.split()
    print(palavra)
    arquivo.write ("\n")

    arquivo.close
'''
def carregarHistorico ():
    arquivo= open("historico.txt", "r")
    lugar=arquivo.readlines()
    x = lugar.split(", ")
    print(x)


'''
hist="a|(198, 275)"
x = hist.split("|")
x3 = x[1]
x3 = x3.replace('(', '')
print(x3)

def salvar_posicao (pos):
    arquivo = open("posicao.txt", "a+")
    arquivo.write(str(pos))
    arquivo.write ("\n")

    arquivo.close

def conversao(delimitador=','):
    tuplas = []
    with open("posicao.txt", 'r') as arquivoP:
        linhas = arquivoP.readlines()
        for linha in linhas:
            elementos = linha.strip().split(delimitador)
            tuplas.append(tuple(elementos))
    return tuplas

def salvar_historico(estrelas, salvarEstrelas):
    with open(salvarEstrelas, 'a+') as arquivo:
        for chave, valor in estrelas.items():
            linha = f"{chave}:{valor}\n"
            arquivo.write(linha)   