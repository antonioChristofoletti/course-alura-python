import random


def imprime_mensagem_abertura():
    print("****************************")
    print("Bem vindo no jogo de Forca!*")
    print("****************************")

def pega_uma_palavra_secreta():
    with open("palavras.txt", "r") as arquivo:
        palavras = [linha for linha in arquivo if linha.strip() != ""]

    return palavras[random.randrange(0, len(palavras))].strip().upper()


def inicializa_letras_acertadas(palavra_secreta):
    return ["_" for _ in palavra_secreta]


def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = -1
    for letra in palavra_secreta:
        index += 1
        if letra == chute:
            letras_acertadas[index] = letra


def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = pega_uma_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while not enforcou and not acertou:
        chute = input("Qual letra?").strip().upper()

        if chute in palavra_secreta:
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print("Ops, Voce errou! Faltam {} tentativas.".format(6 - erros))

        enforcou = erros == 6

        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if acertou:
        print("Voce ganho")
    else:
        print("Voce perdeu")

    print("Fim do jogo")

if __name__ == "__main__":
    jogar()
