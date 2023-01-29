days = int(input('Quantos dias você alugou o carro? '))
km = float(input('Quantos Km foram rodados? '))
pric = (days * 60) + (km * 0.15)
print('Você precisa pagar R${}'.format(pric))