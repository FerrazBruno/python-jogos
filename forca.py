import random


def imprime_mensagem_abertura():
    print('********************************')
    print('***Bem vindo ao jogo da forca***')
    print('********************************')


def carrega_palavra_secreta():
    palavras = []

    with open('jogos/palavras.txt', 'r') as arquivo:
        for palavra in arquivo:
            palavras.append(palavra.strip())

    n = random.randrange(0, len(palavras))
    palavra_secreta = palavras[n].upper()

    return palavra_secreta


def inicializa_letras_acertadas(palavra):
    return ['_' for letra in palavra]


def chutar():
    chute = input('\nQual letra? ').strip().upper()
    return chute


def marca_chute_correto(palavra, chute, letras_acertadas):
    index = 0
    for letra in palavra:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1


def imprime_mensagem_vencedor():
    print('\nParabéns, você ganhou!')
    print("\033[1;33m       ___________      ")
    print("\033[1;33m      '._==_==_=_.'     ")
    print("\033[1;33m      .-\\:      /-.    ")
    print("\033[1;33m     | (|:.     |) |    ")
    print("\033[1;33m      '-|:.     |-'     ")
    print("\033[1;33m        \\::.    /      ")
    print("\033[1;33m         '::. .'        ")
    print("\033[1;33m           ) (          ")
    print("\033[1;33m         _.' '._        ")
    print("\033[1;33m        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print('\nQue pena, você perdeu!')
    print("A palavra era {}".format(palavra_secreta))
    print("\033[1;31m    _______________         ")
    print("\033[1;31m   /               \       ")
    print("\033[1;31m  /                 \      ")
    print("\033[1;31m//                   \/\  ")
    print("\033[1;31m\|   XXXX     XXXX   | /   ")
    print("\033[1;31m |   XXXX     XXXX   |/     ")
    print("\033[1;31m |   XXX       XXX   |      ")
    print("\033[1;31m |                   |      ")
    print("\033[1;31m \__      XXX      __/     ")
    print("\033[1;31m   |\     XXX     /|       ")
    print("\033[1;31m   | |           | |        ")
    print("\033[1;31m   | I I I I I I I |        ")
    print("\033[1;31m   |  I I I I I I  |        ")
    print("\033[1;31m   \_             _/       ")
    print("\033[1;31m     \_         _/         ")
    print("\033[1;31m       \_______/           ")


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not acertou and not enforcou):

        chute = chutar()

        if(chute in palavra_secreta):
            marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7
        acertou = '_' not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    print('\nFim de jogo!')


if (__name__ == '__main__'):
    jogar()
