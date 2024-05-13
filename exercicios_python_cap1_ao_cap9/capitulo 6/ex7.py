alunos = {}

while True:
    nome = input("\nNome do aluno (deixe em branco para sair): ")
    if nome == "":
        break
    nota = float(input("Nota do aluno: "))
    alunos[nome] = nota

notas_arredondadas = {nome: round(nota) for nome, nota in alunos.items()}

print(notas_arredondadas)