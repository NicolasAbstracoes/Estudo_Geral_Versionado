numero_original = int(input('Digite um número entre 0 e 9999: '))

# Separar os dígitos
milhar = numero_original // 1000
centena = (numero_original % 1000) // 100
dezena = (numero_original % 100) // 10
unidade = numero_original % 10
print(milhar)
print(centena)
print(dezena)
print(unidade)
