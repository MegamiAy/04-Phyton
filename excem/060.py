n = float(input('Digite um valor '))
f = n - 1
# 5! = 5 . (n! - 1)
while n == 1:
    n += 1
    fa = n * f
    print('Resultado: {}'.format(fa))