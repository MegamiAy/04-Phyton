n1 = int(input('Um valor: '))
n2 = int(input('Outro Valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
rd = n1 % n2
e = n1 ** n2
print('='*20)
print('A soma é {}, o produto é {} e a divisão é {}'.format(s, m, d))
print('-'*20)
print('A exponenciação é {}, a divisão inteira é {} e o resto da divisão é {}'.format(e, di, rd))
