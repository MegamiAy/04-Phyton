print('Analisador de triângulos 2.0')
a = float(input('Digite o primeiro segmento: '))
b = float(input('Digite o segundo segmento: '))
c = float(input('Digite o terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    print('É possível formar um triângulo:', end='')
    if a == b == c:
        print(' Equilátero')
    elif a != b != c != a:
        print(' Escaleno')
    else:
        print(' Isóceles')
else:
    print('Não é possível formar um triângulo')