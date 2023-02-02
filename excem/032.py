year = int(input('digite quantos dias tem no seu ano atual: '))
da = int(input('Digite o ano em que você está: '))
if year == 366:
    print('{} é um ano bissexto'.format(da))
else:
    print('{} não é um ano bissexto'.format(da))