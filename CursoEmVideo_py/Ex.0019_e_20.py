#Sortear um nome entre 4.

from random import choice, sample

Alunos = ['joao','maria','jose','pedro']
escolhido = choice(Alunos)
escolidos = sample(Alunos,4)
print(escolhido)
print(escolidos)
