from typing import Callable

def transformarLista(lista:int, funcao: Callable[[int], int]) -> list:
    return [funcao(x) for x in lista]


def porExtenso(numero: int) -> str:
    match numero:
        case 0:
            return 'zero'
        case 1:
            return 'um'
        case 2:
            return 'dois'
        case 3:
            return 'tres'
        case 4:
            return 'quatro'
        case 5:
            return 'cinco'
        case 6:
            return 'seis'
        case 7:
            return 'sete'
        case 8:
            return 'oito'
        case 9:
            return 'nove'
        case _:
            return 'numero invalido'


nova_lista = transformarLista([1, 2, 3, 4, 5], porExtenso)

print(nova_lista)