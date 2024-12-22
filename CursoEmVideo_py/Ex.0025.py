#Identifica se o nome da pessoa contem o nome silva

nome_completo = str(input('Me diga seu nome completo: '))

nome_silva = nome_completo.lower().find('silva') != -1

print('A afirmação que seu nome tem silva é: {}'.format(nome_silva))
