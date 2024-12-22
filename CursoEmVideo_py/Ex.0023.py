numero_original = int(input('Digite um número entre 0 e 9999: '))

#Separa os numeros de forma matematica.

milhar = numero_original // 1000
centena = (numero_original % 1000) // 100
dezena = (numero_original % 100) // 10
unidade = numero_original % 10
print(milhar)
print(centena)
print(dezena)
print(unidade)

#Mesmo processo mas com input como str
numero_original_str = str(input('Digite um número entre 0 e 9999: '))

print(numero_original_str[0])
print(numero_original_str[1])
print(numero_original_str[2])
print(numero_original_str[3])