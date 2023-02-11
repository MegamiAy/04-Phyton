s = 0
c = 0
for pi in range(0, 6):
    n = int(input('Digite o {}º número inteiro: '.format(pi)))
    if n % 2 == 0:
        s += n
        c += 1
print('Você informou {} números pares e a soma foi {}'.format(c, s))

