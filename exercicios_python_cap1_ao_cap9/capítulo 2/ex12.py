idade = int(input("Digite a idade: "))
genero = input("Digite o gênero (M/F): ")

if genero == "M" and idade >= 65:
    print("Pode se aposentar")
elif genero == "F" and idade >= 60:
    print("Pode se aposentar")
else:
    print("Não pode se aposentar")