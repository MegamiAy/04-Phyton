from datetime import date

da = int(input('Que ano quer analisar? Digite 0 para analisar o ano atual: '))
if da == 0:
    da = date.today().year

if da % 4 == 0 and da % 100 !=0 or da % 400 == 0:
    print('{} é um ano bissexto'.format(da))
else:
    print('{} não é um ano bissexto'.format(da))
