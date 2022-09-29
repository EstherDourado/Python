raio= float(input('informe o raio: '))
altura= float(input('informe a altura: '))
area= 2 * 3.14 * raio * (altura + raio)
print('area:'.format(area))
litros = area / 3.0
latas = litros / 5.0
print('litros: {}, latas: {}'.format(litros,latas))