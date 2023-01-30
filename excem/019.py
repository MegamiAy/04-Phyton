import random
num = int(input('Digite a quantidade de pessoas para sorteio: '))
sorteio = random.randint(1, num)
print('O sorteado foi o número {}'.format(sorteio))
