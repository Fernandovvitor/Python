largura=float(input('informe a largura da parede:'))
altura=float(input('informa altura da parede:'))
área=largura* altura
print('conforme o valores mostrado {}x{} sua área é {:.2f}'.format(largura,altura,área))
tinta=área/2
print(' o valor da sua área{:.2f} vai ser necessário  isso de litro de  tinta{:.2f}'.format(área,tinta))
