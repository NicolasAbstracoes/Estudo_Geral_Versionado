#Faz o preço de um produto com desconto

produto = str(input('Diga o nome do produto: '))
valor_Original = float(input('Qual o valor original dele: '))
taxa_desconto = float(input('Quantos porcentos dara de desconto: '))

print('O produto {} sairia por {} porem graças a promoção sera apenas por {} com {} porcento de desconto.'.format(produto ,valor_Original ,((1-(taxa_desconto/100))*valor_Original) ,taxa_desconto))
