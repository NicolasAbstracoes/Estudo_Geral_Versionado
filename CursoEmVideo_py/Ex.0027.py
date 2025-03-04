Nome = str(input("Digite seu nome : "))
Primeiro_Nome = Nome.split()[0]
Ultimo_Nome = Nome.split()[len(Nome.split())-1]

print("Seu Primeiro nome é : {}".format(Primeiro_Nome))
print("Seu Ulltimo nome é : {}".format(Ultimo_Nome))