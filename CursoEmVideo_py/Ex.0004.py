#Dissecando uma Variavel

a = input('Digite algo: ')
print('O tipo primitivo do valor é', type(a))
print('O valor digitado é espaços em branco: ', a.isspace())
print('O valor digitado são apenas caracteres numéricos:', a.isnumeric())
print('O valor digitado é alfanuméricos (letras e números): ', a.isalnum())
print('O valor digitado é apenas letras:' , a.isalpha())
print('O valor digitado esta com todas as letras em minúsculo.', a.islower())
