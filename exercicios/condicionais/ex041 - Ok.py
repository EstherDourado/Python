# A configuração nacional de natação precisa de um programa
# que leia o a no de nascimento de um atleta e mostre
# sua categoria de acordo com a idade:
# - Até 9 anos: mirim
# - Até 14 anos:infantil
# - Até 19 anos:junior
# - Até 20 anos: Sénior
# acima:master

from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento


print('Digite sua idade para saber em qual categoria vc pertênce')
idade = int(input('DIGITE AQUI: '))

if idade <= 9:
    print('Sua idade é {}, e você faz parte da categoria Mirim'.format(idade))
elif idade <= 14:
    print('Sua idade é {}, e você faz parte da categoria Infantil'.format(idade))
elif idade <= 19:
    print('Sua idade é {}, e você faz parte da categoria Junior'.format(idade))
elif idade <= 20:
    print('Sua idade é {}, e você faz parte da categoria Sénior'.format(idade))
elif idade > 20:
    print('Sua idade é {}, e você faz parte da categoria Master'.format(idade))

# feito com sucesso
