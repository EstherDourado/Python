# Escreva um programa que leia dois numeros
# inteiros e compare-os, mostrando na tela uma
# mensagem:
# - O primeiro valor é maior
# - O segundo Valor é menor
# - O Não existe valor maior. os dois são  iguais

num1 = int(input('Escreva o primeiro número inteiro: '))
num2 = int(input('Escreva o segundo número inteiro: '))


if num1 > num2:
    print('O primeiro valor {} é maior que o primeiro {}'.format(num1,num2))
elif num2 > num1:
    print('O segundo valor {} é maior que o primeiro {}'.format(num2,num1))
else:
    print('Os dois valores {} e {}, são iguais'.format(num1,num2))

#feito com sucesso