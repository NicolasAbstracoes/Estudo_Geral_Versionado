#Armazena as dimenções de uma parede e calcula a quantidade de tinta em litros utilizada

largura = float(input('Me fale a largura da parede do seu quarto: '))
altura = float(input('Agora me fale a altura dela: '))
area = largura*altura
rend_tinta = 2 #2m quadrados por litro

print('Sua parede tem {} metros quadrados e gastaria {} litros de tinta para ser pintada.'.format(area ,area/rend_tinta))
