import random

def adivinhar_numero():
    try:
        numero = int(input("Digite um número entre 1 e 10: "))
        if numero < 1 or numero > 10:
            raise ValueError("Número fora do intervalo permitido!")
        return numero
    except ValueError as e:
        print(e)
        return adivinhar_numero()	
    
numero_gerado = random.randint(1, 10)
numero_chutado = adivinhar_numero()

if numero_chutado == numero_gerado:
    print("Parabéns, você acertou!")
else:
    print(f"Que pena, o número correto era {numero_gerado}")