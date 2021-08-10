import random


def jogar():
    print('********************************')
    print('Bem vindo ao Jogo da Adivinhação')
    print('********************************')

    numero_secreto = round(random.randrange(1, 101))
    total_tentativas = 0
    pontos = 1000

    print('(1) - Fácil | (2) - Médio | (3) - Difícil')
    nivel = int(input('Defina o nível: '))

    if(nivel == 1):
        total_tentativas = 20
    elif(nivel == 2):
        total_tentativas = 10
    elif(nivel == 3):
        total_tentativas = 5

    for rodada in range(1, total_tentativas+1):
        print('Tentativa {} de {}'.format(rodada, total_tentativas))
        chute = int(input('Digite o seu número entre 1 e 100: '))
        print(f'Você digitou {chute}')

        if(chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100!')
            continue

        acertou = chute == numero_secreto
        menor = chute < numero_secreto
        maior = chute > numero_secreto

        if(acertou):
            print(f'Você acertou e fez {pontos} pontos')
            break
        elif(maior):
            print('Você errou! Chute foi MAIOR do que o número secreto.')
        elif(menor):
            print('Você errou! Chute foi MENOR do que o número escolhido.')

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos

    print('Fim do jogo!')


if(__name__ == '__main__'):
    jogar()
