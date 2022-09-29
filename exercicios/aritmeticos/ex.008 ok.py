#escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
medida = float(input('Coloque uma medida em metros: '))
cm = medida * 100
mm = medida * 1000
print('Em centimentros: {}cm\nEm milimetro: {}mm'.format(cm,mm))
