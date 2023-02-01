vel = float(input('Digite a velocidade que você dirige: '))
mul = (vel - 80) * 7
if vel > 80:
    print('Você está sendo multado, no valor de {} por ter ultrapassado a velocidade limite'.format(mul))
else:
    print('Você não será multado')