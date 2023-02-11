fra = str(input('Digite uma frase: ')).strip().upper()
plv = fra.split()
jun = ''.join(plv)
'''inv = '''''
inv = jun[::]
'''for let in range(len(jun) -1, -1, -1):
    inv += jun[let]'''
print('O inverso de {} é {}'.format(jun, inv))
if inv == jun:
    print('É um palindromo')
else:
    print('Não é um palindromo')