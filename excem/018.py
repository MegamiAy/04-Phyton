from math import radians, cos, sin, tan
num = float(input('Digite o ângulo: '))
ra = radians(num)
cos = cos(ra)
sen = sin(ra)
tan = tan(ra)
print('No ângulo {} \no cosseno é {:.2f} \no seno é {:.2f} \no tangente é {:.2f}'.format(num, cos, sen, tan))
