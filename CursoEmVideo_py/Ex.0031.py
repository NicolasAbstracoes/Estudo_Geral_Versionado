Distancia = int(input("Qual a disntacia da sua viagens em km ?"))
if Distancia <= 200 :
    print("O valor da passagem do onibus vai ser {}".format((Distancia*0.5)))
else:
    print("O valor da passagem do onibus vai ser {}".format((Distancia*0.45)))