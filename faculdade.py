##funções##
def pede_idade(mensagem):
    idade=int(input(mensagem))
    return idade

##codigo principal##
idade= pede_idade('digite sua idadade')
if idade>18:
    print('você tem mais de 18 anos')
else:
    print('você tem menos de 18 anos')
    print('fim')


