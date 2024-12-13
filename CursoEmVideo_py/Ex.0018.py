#Mostra o sen, cos e tan de um angulo

from math import cos ,tan ,sin ,radians

angulo = int(input("Digite um algulo qual quer: "))

print('O coseno do angulo é {}. \nO seno do angulo é {}. \nA tangente do angulo é {}. \n'.format(cos(radians(angulo)),sin(radians(angulo)),tan(radians(angulo))))
