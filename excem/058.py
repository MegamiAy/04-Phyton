'''from random import randint
pc = randint(0, 10)
print('O computador pensou em um número, tente acertar')
res = ''
ten = ''
while res != pc:
    res = int(input('Digite sua tentativa: '))
    ten += 1
print('Foram necessárias {} tentativas para você acertar'.format(ten))'''

from random import randint
pc = randint(0, 10)
print('O computador pensou em um número, tente acertar')
ac = False
te = 0
while not ac:
    jg = int(input('Digite seu palpite'))
    te += 1
    if jg == pc:
        ac = True
    else:
        if jg < pc:
            print('Mais...')
        elif jg > pc:
            print('Menos...')
print('Acertou')
print('Foram {} tentativas para acertar'.format(te))
