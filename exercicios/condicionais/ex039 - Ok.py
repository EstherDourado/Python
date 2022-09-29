# faça um programa que leia o ano de nascimento
# de um jovem e informe, de acordo com sua idade
#- se ele ainda vai se alistar ao serviço militar
# - se é a hora de se alistar
# - se já passou do tempo do alistamento.
#deve mostrar o tempo que falta ou que passou do prazo.

ano= int(input('Em que ano vc nasceu?: '))
alistamento= 2022 - ano

if alistamento == 18:
    print('É hora de se alistar')
elif alistamento < 18:
    print('Falta {} anos para vc se alistar'.format(18 - alistamento))
    print('Você se alistara em {}'.format(ano + 18))
elif alistamento > 18:
    print('Já passou {}, da hora de se alistar'.format(alistamento - 18))

#feito com sucesso