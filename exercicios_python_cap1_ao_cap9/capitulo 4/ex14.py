import re

frase = input("Digite uma frase: ")
palavras = re.findall(r"\w+", frase)

for palavra in palavras:
    print(f"A palavra {palavra} começa na posição {frase.index(palavra)}")

