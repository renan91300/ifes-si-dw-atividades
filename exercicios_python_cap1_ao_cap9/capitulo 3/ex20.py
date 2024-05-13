n = int(input("Digite um número: "))

for i in range(1, n+1):
    fatorial = 1
    for j in range(1, i+1):
        fatorial *= j
    print(f"O fatorial de {i} é {fatorial}")