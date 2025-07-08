from operator import truediv

total=0
quero_comprar=True
while quero_comprar:
    preco=float(input('preço'))
    total += preco
    opcao= input('continuar comprando (s/n')
    if opcao != 's':
        quero_comprar:False
        print(f' total da compra R$ {total:.22f}')