from random import choice
Numero_Aleatorio = choice(range(5))


Chute = int(input("Pensei em um numero pseudo-aleatorio, entre 0 e 5. Tente adivinhar qual :"))
if Chute == Numero_Aleatorio:
    print("Parabens Voce acertou!!")
else:
    print("Errou, uma pena.")
print("Eu pensei no numero {}".format(Numero_Aleatorio))