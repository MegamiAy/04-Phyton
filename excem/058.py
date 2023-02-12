from random import randint
pc = randint(0, 10)
print('O computador pensou em um número, tente acertar')
res = ''
ten = ''
while res != pc:
    res = int(input('Digite sua tentativa: '))
    res += 1
print('Foram necessárias {} tentativas para você acertar'.format(res))
