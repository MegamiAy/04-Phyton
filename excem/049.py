n = int(input('Digite o número que quer a tabuada: '))
print('-='*6)
for t in range(1, 10+1):
    print('{} x {} = {}'.format(n, t, n*t))
print('-='*6)
