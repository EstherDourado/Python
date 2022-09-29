#Desenvolva um programa que pergunte a distancia de uma viagem em km. calcule o preço da passagem.
#cobrando 0,50 por km para viagens de até 200km e 0,45 para viagens mais longas.
distancia = float(input('Qual a distância que você quer calcular?: '))
if distancia <= 200:
    p1 = distancia * 0.50
else:
    p1 = distancia * 0.45
print('O preço da sua viajem é R${:.2f}'.format(p1))


# feito