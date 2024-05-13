numeros = []
for i in range(10):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

numeros.sort()

print(f"O segundo menor número é {numeros[1]}")
print(f"O segundo maior número é {numeros[-2]}")