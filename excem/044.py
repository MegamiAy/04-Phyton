pric = float(input('Preço das compras R$'))
print('''Forma de Pagamento
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
fom = int(input('Qual a opção de pagamento? '))
if fom == 1:
    tot = pric - (pric * 10 / 100)
elif fom == 2:
    tot = pric - (pric * 5 / 100)
elif fom == 3:
    tot = pric
    par = tot / 2
    print('Sua compra será parcelada em 2x de R${}'.format(par))
elif fom == 4:
    qpar = int(input('Qauntas parcelas serão? '))
    tot = pric + (pric * 20 / 100)
    par = tot / qpar
    print('Sua compra será parcelada em {}x de R${}'.format(qpar, par))
else:
    print('Opção inválida')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(pric, tot))
