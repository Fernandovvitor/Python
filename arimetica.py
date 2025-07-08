N1=int(input('digite um valor'))
N2=int(input('outro valor'))
s=N1+N2
d=N1/N2
m=N1*N2
e=N1**N2
r=N1//N2
print('a soma vale {}, \n o produto é {}  a divisão é\n {}'.format(s,m,d),end='')
print('a exponeação{:.2f} a d3ivisão real é {:.3f}' .format(e,r))