from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
yo = int(input('escolha sua opção: '))
print('Computator escolheu {}'.format(itens[pc]))
print('Você escolheu {}'.format(itens[yo]))
if pc == 0:
    if yo == 0:
        print('Empate')
    elif yo == 1:
        print('Vitória do jogador')
    elif yo == 2:
        print('Vitória do computador')
    else:
        print('Jogada inválida')
elif pc == 1:
    if yo == 0:
        print('Vitória do computador')
    elif yo == 1:
        print('Empate')
    elif yo == 2:
        print('Vitória do jogador')
    else:
        print('Jogada inválida')
elif pc == 2:
    if yo == 0:
        print('Vitória do Jogador')
    elif yo == 1:
        print('Vitória do computador')
    elif yo == 2:
        print('Empate')
    else:
        print('Jogada inválida')
print('Fim de jogo')