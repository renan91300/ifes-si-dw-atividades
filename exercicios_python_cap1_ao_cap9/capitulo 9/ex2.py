def calcular_media(numeros: list) -> float:
    try:
        return sum(numeros) / len(numeros)
    except ZeroDivisionError:
        print("A lista está vazia!")
    except TypeError:
        print("A lista contém elementos que não são números!")


numeros = [1, 2, 3, "2", 3]
media = calcular_media(numeros)

print(media)