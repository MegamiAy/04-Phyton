n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
me = (n1 + n2)/2
print('Sua média é: {}'.format(me))
if me >= 7:
    print('Sua média está aceitável')
else:
    print('Sua média não é o suficiente')
print('Continue estudando')
