a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))

delta = (b ** 2) - 4 * a * c

if delta < 0:
    print("A equação não possui raízes reais.")

elif delta == 0:
    raiz = -b / (2 * a)
    print(f"A raiz da equação é {raiz}.")
else:
    raiz1 = (-b + delta ** 0.5) / (2 * a)
    raiz2 = (-b - delta ** 0.5) / (2 * a)
    print(f"As raízes da equação são {raiz1} e {raiz2}.")

