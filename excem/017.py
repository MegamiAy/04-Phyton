from math import hypot
x = float(input('digite o comprimento do cateto oposto: '))
y = float(input('digite o comprimento do cateto adjacente: '))
h = hypot(x, y)
print('A hipotenusa é {:.2f}'.format(h))
