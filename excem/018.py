import math
num = float(input('Digite o ângulo: '))
ra = math.radians(num)
cos = math.cos(ra)
sen = math.sin(ra)
tan = math.tan(ra)
print('No ângulo {} \no cosseno é {:.2f} \no seno é {:.2f} \no tangente é {:.2f}'.format(num, cos, sen, tan))
