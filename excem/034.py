mon = float(input('Qual é o salário do funcionário? R$'))
if mon <= 1250:
    aum = mon + (mon * 15/100)
else:
    aum = mon + (mon * 10/100)
print('O novo sálario será R${}'.format(aum))
