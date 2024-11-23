# Função para aplicar a cifra de César
def cifra_de_cesar(mensagem, deslocamento):
    mensagem_cifrada = ""
    for caractere in mensagem:
        # Verificar se é uma letra maiúscula
        if 'A' <= caractere <= 'Z':
            nova_letra = chr((ord(caractere) - ord('A') + deslocamento) % 26 + ord('A'))
            mensagem_cifrada += nova_letra
        # Verificar se é uma letra minúscula
        elif 'a' <= caractere <= 'z':
            nova_letra = chr((ord(caractere) - ord('a') + deslocamento) % 26 + ord('a'))
            mensagem_cifrada += nova_letra
        else:
            # Mantem qualquer outro caractere
            mensagem_cifrada += caractere
    return mensagem_cifrada


# Programa principal
print("=== Cifra de César ===")
frase = input("Digite uma frase: ")
deslocamento = int(input("Digite um número de deslocamento: "))

# Chama a função e exibe o resultado
resultado = cifra_de_cesar(frase, deslocamento)
print(f"\nMensagem cifrada: {resultado}")