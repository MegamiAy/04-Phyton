m1 = float(input('Digite a sua primeira nota: '))
m2 = float(input('Digite a sua segunda nota: '))
me = (m1 + m2) / 2
if me >= 7:
    print('Aprovado')
elif 7 > me >= 5: # ou me >= 5 and me < 7
    print('Recuperação')
elif me < 5: # ou else:
    print('Reprovado')
