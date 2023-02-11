mediaidade = 0
somaidade = 0
maioridadeh = 0
nomevelho = 0
tmulher20 = 0
for p in range(1, 5):
    print('--- {}ª Pessoa ---'.format(p))
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        tmulher20 += 1
mediaidade = somaidade / 4
print('A média de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho tem {} anos e seu nome é {}'.format(maioridadeh, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(tmulher20))
