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
