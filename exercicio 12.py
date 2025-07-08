n1=float(input('informe o produto que deseja o desconto:'))
desconto=(n1*5)/100
print('sua compra receberá o desconto {:.2f}'.format(desconto))
valorfinal=n1-desconto
print('o seu produto ficara nesse valor{}'.format(valorfinal))
