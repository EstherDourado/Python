#crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar.
numero= int(input('Escreva um número inteiro: '))
impar = numero % 2
par = numero % 2
if par == 0:
    print('Essse numero {} é par'.format(numero))
else:
    print('Esse numero {} é impar'.format(numero))