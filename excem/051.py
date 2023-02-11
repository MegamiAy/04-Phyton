te = int(input('Digite o valor do primeiro termo: '))
ra = int(input('Digite o valor da razão: '))
de = te + (10 - 1) * ra
for pa in range(te, de+ra, ra):
    print('{}'.format(pa), end='-> ')
print('ACABOU')