km = float(input('Digite a distância da sua viagem em Km: '))
du = km*0.45
me = km*0.50
if km > 200:
    print('o valor da viagem de até 200km será: {}'.format(du))
else:
    print('o valor da viagem será de: {}'.format(me))
print('Boa viagem')
