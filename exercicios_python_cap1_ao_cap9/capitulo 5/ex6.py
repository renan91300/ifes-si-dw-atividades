import random

idades = [2, 16, 26, 66, 34]

def adicionar(lista: list) -> list:
    lista.append(random.randint(1, 120))
    return lista

idades = adicionar(idades)

print(idades)