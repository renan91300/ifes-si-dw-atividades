numeros = []
while True:
    numero = int(input("Digite um número: "))
    if numero < 0:
        break
    numeros.append(numero)

if numeros:
    media = sum(numeros) / len(numeros)
    print(f"A média dos números digitados é {media}.")
else:
    print("Nenhum número foi digitado.")
