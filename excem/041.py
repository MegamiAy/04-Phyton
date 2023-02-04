from datetime import date
nasc = int(input('Digite o seu ano de nascimento: '))
atu = date.today().year
age = nasc - atu
print('Você tem {} anos'.format(age))
if age <= 9:
    print('Mirim')
elif age <= 14:
    print('Infantil')
elif age <= 19:
    print('Junior')
elif age <= 25:
    print('Sênior')
else:
    print('Master')
print('Fim...')