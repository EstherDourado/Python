#desenvolva um programa que leia seis números
#inteiros e mostre a soma daqueles que forem pares.
#Se o valor digitado for impar desconsidere-o.

soma = 0
cont = 0
for c in range(1,7):
    n = int(input('Coloque {} número: '.format(c)))
    if n % 2 == 0:
        soma += n
        cont += 1
print('Você digitou {} números pares, e a soma deles são {}'.format(cont, soma))

