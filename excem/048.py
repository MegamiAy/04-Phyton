soma = 0
cont = 0
for som in range(1, 501, 2):
    if som % 3 == 0:
        cont += 1 # cont = cont + 1
        soma += som # soma = soma + som
print('A soma dos {} valores solicitados é {}'.format(cont, soma))
