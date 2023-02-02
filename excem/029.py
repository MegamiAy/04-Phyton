vel = float(input('Digite a velocidade atual do seu veiculo: '))
mul = (vel - 80) * 7
if vel > 80:
    print('Você está sendo multado, no valor de {} por ter ultrapassado a velocidade limite'.format(mul))
else:
    print('Você não será multado')