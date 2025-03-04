Ano = int(input("Me fale um ano e falarei se é bissexto: "))

dezena = str((Ano % 100) // 10)
unidade = str(Ano % 10)
D_U = dezena + unidade
if D_U != "00":
    if Ano%4 == 0:
        print("Esse é um ano Bissexto!")
    else:
        print("Esse não é um ano Bissexto!!")
else:
    if Ano%400 == 0:
     print("Esse é um ano Bissexto!!")
    else:
       print("Esse não é um ano Bissexto!!")


print(Ano%4)
print(Ano%400)