from datetime import date
tod = date.today().year
tma = 0
tme = 0
for per in range(1, 8):
    yea = int(input('Em que ano a {}ª pessoa nasceu? '.format(per)))
    age = tod - yea
    if age >= 21:
        tma += 1
    else:
        tme += 1
print('Ao todo tivemos {} pessoas maior de idade'.format(tma))
print('Ao todo tivemos {} pessoas menor de idade'.format(tme))
