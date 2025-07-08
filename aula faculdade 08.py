n=int(input('digite um número'))
divisor= 2
while divisor<n:
    print(f'{n} % {divisor}={n % divisor}')
    if n% divisor == 0:
        break
    divisor +=1
if divisor==n:
    print('primo')

else:
    print('não é um numero primo')
    print('Os matemáticos então decidiram excluir o número 1 do grupo dos primos para que o teorema fosse preservado!')