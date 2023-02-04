alt = float(input('Digite sua altura em metros: '))
pes = float(input('Digite seu peso em quilos: '))
imc = pes / (alt ** 2)
print('Seu IMC é de {:.2f}'.format(imc))
if imc < 18.5:
    print('abaixo do peso')
elif 18.5 <= imc < 25:
    print('peso ideal')
elif 25 <= imc < 30:
    print('sobre peso')
elif 30 <= imc < 40:
    print('obesidade')
else:
    print('obesidade mórbida')
