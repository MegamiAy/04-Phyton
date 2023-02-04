m1 = float(input('Digite a sua primeira nota: '))
m2 = float(input('Digite a sua segunda nota: '))
me = (m1 + m2) / 2
if me >= 7:
    print('Aprovado')
elif me >= 5 and me <= 6.9:
    print('Recuperação')
elif me < 5:
    print('Reprovado')
