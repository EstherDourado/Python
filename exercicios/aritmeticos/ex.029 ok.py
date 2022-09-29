# escreva um programa que leia a velocidade de um carro se ele ultrapassar 80km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar 7 reais por cada km acima do limite.

velocidade = float(input('Qual é a velocidade do carro?: '))
if velocidade > 80:
    print('Você ultrapassou o limite de velocidade')
    multa = (velocidade - 80) * 7
    print('Você pagara uma multa de R${:.2f}'.format(multa))
print('Tenha um bom dia! Dirija com segurança!')