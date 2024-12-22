#Manipulação de txt

nome = str(input('Digite um seu nome completo: '))

nome_maior = nome.upper()
nome_menor = nome.lower()
nome_num = nome.replace(" " ,"")
nome_num_Primeiro = nome.split()


print(nome)
print(nome_maior)
print(nome_menor)
print(len(nome_num))
print(len(nome_num_Primeiro[0]))


