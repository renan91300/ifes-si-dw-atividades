frase = input("Digite uma frase: ")

palavras = [palavra.replace("a", "o") for palavra in frase.split() if "a" in palavra]

print(palavras)