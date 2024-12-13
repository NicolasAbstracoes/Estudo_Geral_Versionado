#Aluguel de carros onde o dia é 60 e o km 0,15.

dias_alugasdos = int(input('Quantos dias voce ficou com o carro? '))
km_rodados_inicio = int(input('Qual foi o km inicial ?'))
km_rodados_final = int(input('Qual foi o km final ?'))

print('O valor a ser pago é R${} .'.format(dias_alugasdos*60+0.15*(km_rodados_final-km_rodados_inicio)))
