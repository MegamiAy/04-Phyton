name = str(input('Digite seu nome completo: ')).strip()
snam = name.split(' ')
print('Primeiro nome: {}'.format(snam[0]))
print('Segundo nome: {}'.format(snam[len(snam)-1]))
