import forca
import adivinhacao


def jogos():
    print("****************************")
    print("Escolha o seu jogo!*********")
    print("****************************")

    print("(1) Forca (2) Adivinacao")

    jogo = int(input("Qual o jogo?"))

    if jogo == 1:
        print("Jogando forca")
        forca.jogar()
    elif jogo == 2:
        print("Jogando adivinhacao")
        adivinhacao.jogar()


if __name__ == "__main__":
    jogos()
