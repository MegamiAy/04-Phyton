import random

num = random.randint(0, 5)
res = int(input('Chute um número de 0 a 5: '))

if res == num:
    print('Você acertou')
else:
    print('Você errou')
print('O número é: {}'.format(num))
