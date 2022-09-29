#faça um programa que leia um numero inteiro
# e diga se ele pe ou não um número primo

# NUMEROS PRIMOS - SÃO NÚMEROS NATURAIS QUE PODEM SER DIVIDIDOS POR 1 E POR ELE MESMO.

num = int(input('Digite um número: '))
tot = 0
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[33m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[m O número {} foi divisivel {} vezes'.format(num,tot))
if tot == 2:
    print('Esse número é PRIMO!!!')
else:
    print('Esse número NÃO é primo!')