km = float(input('Digite a distância da sua viagem em Km: '))
if km > 200:
    price = km*0.45
else:
    price = km*0.50
print('Sua viagem custará {}! Boa viagem'.format(price))
