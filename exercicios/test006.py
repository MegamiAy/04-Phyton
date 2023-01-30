import math
num = int(input('Digite um número: '))
rq = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, math.ceil(rq)))
