'''from math import factorial
n = float(input('Digite um valor para calcular seu fatorial '))
f = factorial(n)
# 5! = 5 . (n! - 1)'''
n = int(input('Digite um valor para calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
