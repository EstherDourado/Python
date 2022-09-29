#Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o
# usuario tentar descobrir qual foi o numero escolhido pelo computador. o programa devera escrever na tela
# se o usuario venceu ou perdeu.

from random import randint #random escolhe coisas no aleatorias
from time import sleep
print('-=-' * 20)
computador = randint(0,10) #faz o computador escolher um numero
jogador= int(input('Pensei em um numero entre 0 e 5 tente adivinhar... ')) #jogador tenta adivinhar
print('Processando...')
sleep(1)
print('-=-' * 20)
if jogador == computador:
    print('Parabens, você conseguiu me vencer')
else:
    print('Ganhei!, eu pensei no numero {}, e não no {}'.format(computador, jogador))


#feito