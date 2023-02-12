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
        print(n1 + n2)
    elif op == 2:
        print(n1 * n2)
    elif op == 3:
        if n1 > n2:
            print('O primeiro valor é o maior')
        else:
            print('O segundo valor é o maior')
    elif op == 4:
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))
    elif op == 5:
        print('Fim')
    else:
        print('Opção inválida')