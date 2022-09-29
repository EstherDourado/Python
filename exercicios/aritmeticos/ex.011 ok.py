#Nome: Esther Dourado Batista RGM:30038693

raio = float(input('Raio da parede: '))
alt = float(input('Altura da parede: '))

base = (3.14 * (raio ** 2))
lateral = (2 * 3.14 * raio * alt)
cilindro = 2 * base + lateral
litros = cilindro/3
latas = litros/5
precoLatas = latas * 50

print('É preciso de {:.0f} latas de tinta, que da um total de R${:.2f}'.format(latas,precoLatas))
print('Cilindro tem {} m2'.format(cilindro))

#feito