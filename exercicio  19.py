import random

a1=input(str('informe nome de um aluno?'))
a2=input(str('informe nome de outro aluno'))
a3=input(str('informe nome de outro aluno'))
alunos= [a1,a2,a3]
sorteado= random.choice(alunos)
print('o aluno sorteado é {}'.format(sorteado))