km = float(input('Digite a distância da sua viagem em Km: '))
du = km*0.45
me = km*0.50
if km > 200:
    print('o valor da viagem acima de 200km será: {}'.format(me))
else:
    print('o valor da viagem será de: {}'.format(du))
print('Boa viagem')
