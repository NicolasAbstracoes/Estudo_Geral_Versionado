#Da um aumento no salario de alguem

salario_inicial = float(input('Diga o salario inicial do funcionario? '))
taxa_Aumento = float(input('Quantos porceto deseja aumentar apos 1 ano? '))

print('O novo salario sera no valor de {}.'.format((1+(taxa_Aumento/100))*salario_inicial))
