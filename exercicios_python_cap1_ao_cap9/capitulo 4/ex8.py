import re

while True:
    frase = input("Digite uma frase com 5 palavras: ")
    palavras = re.findall(r"\w+", frase)

    if len(palavras) == 5:
        for palavra in palavras:
            print(palavra)
        break
    print("Frase inválida. Digite novamente.")
