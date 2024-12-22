# Identifica a posição da primeira e ultima aparição da letra "a"

frase = str(input('Digite uma frase: ')).strip().lower()

print("A frase {} possui {} letras 'a'sendo a primeira na posição {} e a ultima na posição {}.".format(frase ,frase.count("a") ,frase.find("a")+1 ,frase.rfind("a")+1))


