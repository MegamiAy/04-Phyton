bigger = 0
smaller = 0
for person in range(1, 6):
    weight = float(input('Peso da {}ª pessoa: '.format(person)))
    if person == 1:
        bigger = weight
        smaller = weight
    else:
        if weight > bigger:
            bigger = weight
        if weight < smaller:
            smaller = weight
print('O maior peso lido foi de {}Kg'.format(bigger))
print('O menor peso lido foi de {}Kg'.format(smaller))
