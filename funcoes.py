

def historico(item,pos):
    arquivo = open("historico.txt", "a+") 
    arquivo.write (item)
    arquivo.write(",")
    arquivo.write(str(pos))
    palavra =item.split()
    print(palavra)
    arquivo.write ("\n")

    arquivo.close
