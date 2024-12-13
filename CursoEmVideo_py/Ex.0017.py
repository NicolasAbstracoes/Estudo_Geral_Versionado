#Calculando a Hipotenusa

from math import sqrt

cateto_ad = float(input('Me fale o cateto adijacente de um triangulo retangulo: '))
cateto_op = float(input('Me fale o cateto oposto de um triangulo retangulo:  '))
hipotenusa = cateto_op*cateto_op+cateto_ad*cateto_ad
print('A hipotenusa é igual a {}.'.format(sqrt(hipotenusa)))
