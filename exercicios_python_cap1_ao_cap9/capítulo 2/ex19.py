import random

numero = random.randint(1, 10)

chute = int(input("Adivinhe o número entre 1 e 10: "))

if chute == numero:
    print("Parabéns! Você acertou!")
else:
    print(f"Que pena! O número era {numero}.")