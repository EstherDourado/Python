#desenvolva um programa que leia o primeiro
#termo e a razão de uma PA. No final, mostre
#os 10 primeiros termos dessa progressão.

pTermo = int(input('Digite o 1° termo: '))
razao =  int(input('Digite a razão: '))
pa = pTermo + (10-1) * razao
for c in range(pTermo,pa + razao ,razao):
    print('{} '.format(c), end='-> ')
print('ACABOU')





