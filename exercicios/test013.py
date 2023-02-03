name = str(input('Qual é seu nome? '))
if name == 'Gustavo':
    print('Que nome bonito')
elif name == 'Pedro' or name == 'Maria' or name == 'João':
    print('Seu nome é bem popular no Brasil')
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}'.format(name))
