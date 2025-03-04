Limite_Velocidade = 80
Velocidade = int(input("A que velocidade voce estava de carro ?"))
Valor_Multa = (Velocidade-80)*7

if Velocidade > Limite_Velocidade:
    print("Voce foi multado em {} reais".format(Valor_Multa))