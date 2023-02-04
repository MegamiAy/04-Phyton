num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
if num1 > num2:
    maior = num1
    print('O primeiro valor ({}) é maior'.format(num1))
elif num2 > num1:
    maior = num2
    print('O segundo valor ({}) é maior'.format(num2))
else:
    print('Não existe valor maior, os dois são iguais')
