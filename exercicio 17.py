import math
co=float(input('cumprimento do cateto opost:'))
ca= float(input('cumprimento do cateto adjacente '))
hi= math.hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))