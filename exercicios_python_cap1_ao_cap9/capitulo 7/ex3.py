with (open("arquivo_ex3.txt", "r", encoding="utf-8")) as arquivo:
    linha = arquivo.readline()
    while linha:
        with open("arquivo_ex3_invertido.txt", "a", encoding="utf-8") as arquivo_invertido:
            arquivo_invertido.write(linha[::-1] + '\n')
        linha = arquivo.readline()
