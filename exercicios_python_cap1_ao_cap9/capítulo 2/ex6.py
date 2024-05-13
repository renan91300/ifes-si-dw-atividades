texto = input("Digite um texto: ")

if texto == texto[::-1]:
    print("O texto é um palíndromo.")
else:
    print("O texto não é um palíndromo.")