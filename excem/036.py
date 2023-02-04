pri = float(input('Digite o valor da casa R$'))
mon = float(input('Digite seu salário R$'))
yea = float(input('Digite em quantos anos você irá pagar: '))
pre = pri / (yea * 12) # prestação
neg = mon * 30 / 100
print('Para pagar um casa de R${:.2f} em {} anos'.format(pri, yea), end='')
print(' a prestação será de R${:2f}'.format(pre))
if pre <= neg:
    print('Empréstimo pode ser consedido')
else:
    print('Empréstimo negado')
