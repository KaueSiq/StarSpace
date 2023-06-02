

def historico(item,pos):
    arquivo = open("historico.txt", "a+") 
    arquivo.write (item)
    arquivo.write(str(pos))
    arquivo.write ("\n")
    #arquivo.write(str(pos))
    #arquivo.write ("\n")

    arquivo.close