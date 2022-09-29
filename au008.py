#utilizando modulos
#quando eu não especifico o que eu quero importa, vem todos os modulos da biblioteca
from math import sqrt
n = int(input('Digite um Número: '))
raiz = sqrt(n)
print('A raiz de {} é igual a {}'.format(n,ceil(raiz)))
#ceil- é o arredondamento para cima
#floor- é o arredondamento para baixo
'''para que não seja necessario chamar uma biblioteca,
eu coloco no começo do codigo - from math import sqrt - '''


