age = int(input('Digite sua idade: '))
pas = age - 18
ant = 18 - age
if age == 18:
    print('É hora de se alistar ao serviço militar')
elif age < 18:
    print('Você ainda irá se alistar no exercito, ainda falta {} ano(s)'.format(ant))
else:
    print('Já passou do tempo do seu alistamento no exercito, se passou {} ano(s)'.format(pas))
