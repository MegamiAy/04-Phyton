S = ''
while S != 'F' and 'M':
    S = str(input('Digite seu sexo: [F/M]')).upper()
    if S == 'F':
        print('Você é uma mulher')
    elif S == 'M':
        print('Você é um homem')