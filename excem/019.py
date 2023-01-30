import random
'''num = int(input('Digite a quantidade de pessoas para sorteio: '))
sorteio = random.randint(1, num)
print('O sorteado foi o número {}'.format(sorteio))'''

n1 = input('Primeiro aluno: ')
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = input('Quarto aluno: ')
list = [n1, n2, n3, n4]
choosed = random.choice(list)
print('o aluno escolhido foi {}'.format(choosed))
