#crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.
numero= int(input('Escreva um numero: '))
d= numero * 2
t= numero * 3
r= numero ** (1/2)
print('Dobro: {}\nTriplo: {}\nRaiz Quadrada:{:.2f}\n'.format(d,t,r))