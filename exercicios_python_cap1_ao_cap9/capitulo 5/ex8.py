alfabeto = 'abcdefghijklmnopqrstuvwxyz'

def decifrar_mensagem(mensagem: str) -> str:
    if mensagem == '':
        return ''
    else:
        if mensagem[0] == 'z':
            return 'a' + decifrar_mensagem(mensagem[1:])
        else:
            if mensagem[0] not in alfabeto:
                return mensagem[0] + decifrar_mensagem(mensagem[1:])
            return alfabeto[alfabeto.index(mensagem[0]) - 1] + decifrar_mensagem(mensagem[1:])


mensagem_codificada = input("Digite a mensagem codificada: ")

print("A mensagem decodificada é: ", decifrar_mensagem(mensagem_codificada))