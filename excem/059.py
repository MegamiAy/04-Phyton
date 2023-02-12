n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
op = ''
print('''Menu
[ 1 ] Somar
[ 2 ] Multiplicar 
[ 3 ] Maior
[ 4 ] Novos números
[ 5 ] Sair do programa''')
while op != 5:
    op = int(input('Digite sua escolha: '))
    if op == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif op == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif op == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        elif n2 > n1:
            print('{} é maior que {}'.format(n2, n1))
        else:
            print('Não há números maiores, ambos são iguais')
    elif op == 4:
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))
    elif op == 5:
        print('Fim')
    else:
        print('Opção inválida')