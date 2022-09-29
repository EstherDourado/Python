#Nome: Esther Dourado Batista RGM:30038693

nome=str(input('Digite o nome do aluno: '))
P1= float(input('digite a nota P1: '))
P2= float(input('digite a nota P2: '))
media= float(P1+P2)/2
print('{} sua notas são P1:{} e P2:{} e sua media é {}'.format(nome,P1,P2,media))

if media >=6:
    print('Parabens você foi Aprovado')
elif media <=4:
    print('Você foi para Recuperação')
else:
    print('Você foi Reprovado')

#feito

