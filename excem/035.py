print('-_' * 15)
print('Analisador de Triângulos v1.0')
print('-_' * 15)
a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentoss acima podem formar um triângulo')
else:
    print('Os segmentos acima não podem forma um triângulo')
