#crie um programa que jogue jokenpo com vc
from random import randint
from time import sleep

itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')

print('-=' * 10)
print('Computador jogou {}'.format('\033[0;3;32m', itens[computador],'\033[0;3;32m'))
print('Jogador jogou {}'.format('\033[0;3;33m',itens[jogador],'\033[0;3;33m'))
print('-=' * 10)
if computador == 0: # COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print('DEU EMPATE')
    elif jogador == 1:
        print('JOGADOR GANHOU!!!')
    elif jogador == 2:
        print('COMPUTADOR GANHOU!!!')
    else:
        print('JOGADA INVALIDA')
elif computador == 1: #COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print('COMPUTADOR GANHOU')
    elif jogador == 1:
        print('DEU EMPATE!!!')
    elif jogador == 2:
        print('JOGADOR GANHOU!!!')
    else:
        print('JOGADA INVALIDA!')
elif computador == 2: # COMPUTADOR JOGOU TESOURA
        if jogador == 0:
            print('JOGADOR GANHOU')
        elif jogador == 1:
            print('COMPUTADOR GANHOU!!!')
        elif jogador == 2:
            print('DEU EMPATE!!!')
        else:
            print('JOGADA INVALIDA')
