S = str(input('Digite seu sexo: [F/M]')).strip().upper()[0]
while S not in 'FM':
    S = str(input('Dado inválido. Digite novamente: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(S))
