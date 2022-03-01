import random


def jogar():
    numero_secreto = random.randrange(1, 101)
    pontos = 1000

    print("*********************************")
    print("Bem vindo no jogo de Adivinhacao*")
    print("*********************************")

    print("O número secreto é {}".format(numero_secreto))
    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Define o nível: "))

    if nivel == 1:
        maxTentativa = 20
    elif nivel == 2:
        maxTentativa = 10
    else:
        maxTentativa = 5

    for tentativa in range(1, maxTentativa + 1):
        print("Tentativa {} de {:.2f}".format(tentativa, maxTentativa))

        chute = int(input("Digite o seu número: "))

        if chute <= 0 or chute > 100:
            print("Valor deve estar entre 0 e 100")
            continue

        print("Você digitou", chute)

        if numero_secreto == chute:
            print("Voce acertou e fez {} pontos!".format(pontos))
            break
        elif chute > numero_secreto:
            print("Voce errou! O seu chute foi maior do que o numero secreto")
        else:
            print("Voce errou! O seu chute foi menor do que o numero secreto")

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos


if __name__ == "__main__":
    jogar()
