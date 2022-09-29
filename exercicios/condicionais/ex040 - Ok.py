# crie um programa que leia duas notas de um aluno
# e calcule sua media. mostrando uma mensagem no final,
# de acordo com a média atingida:
# - Média abaixo de 5.0:Reprovado
# - Média entre 5.0 e 6.9: Recuperação
# - Média 7.0 ou superior: Aprovado

nota1 = (float(input('Digite sua primeira nota: ')))
nota2 = (float(input('Digite sua segunda nota: ')))
soma = (nota1 + nota2)/2
print('As notas {}, e {} tem uma media de {}'.format(nota1,nota2,soma))
if soma <= 5.0:
    print('Você foi reprovado')
elif soma > 5.0 <= 6.9:
    print('Você ficou de recuperação')
elif soma >= 7.0:
    print('Você foi aprovado')

#feito 