# identificando se a cidade do input começa com santo

cidade = str(input('Digite o nome da sua cidade: ')).strip()

comeco_nome = cidade.lower().split()
print("A afirmação que sua cidade começa com a palavra santo é : ",comeco_nome[0] == "santo")
