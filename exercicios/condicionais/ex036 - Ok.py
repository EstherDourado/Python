# Escreva um programa para aprovar o emprestimo bancario
# para a compra de uma casa. O programa vai pergunbtar
# o valor da casa, o salario do comprador e em quantos
# anos ele vai pagar.
# calcule o valor da prestação mensal, sabendo que ela
# não pode exceder 30% do salário ou então o empréstimo
# será negado.

v_casa = float(input('Qual o valor da casa?: '))
m_salario = float(input('Qual sua media salarial?: '))
anos = int(input('Quantos anos vai pagar?: '))

prestacao = v_casa/(anos * 12)
minimo = m_salario * 30/100

print('Para uma casa de R${:.2f} em {} anos'.format(v_casa,anos), end='')
print(' a prestação será de R${:.2f}'.format(prestacao))

if prestacao <= minimo:
    print('Emprestimo aprovado')
else:
    print('Emprestimo negado')

#feito