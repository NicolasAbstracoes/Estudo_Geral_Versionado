N1 = int(input("Digite um valor :"))
N2 = int(input("Digite um valor :"))
N3 = int(input("Digite um valor :"))

if N1 >= N2 and N1 >= N3 and N2 >= N3:
    print("O numero {} é o maior.E {} é o menor.".format(N1, N3)) 
elif N1 >= N2 and N1 >= N3 and N3 >= N2:
    print("O numero {} é o maior.E {} é o menor.".format(N1, N2))
elif N1 <= N2 and N1 <= N3 and N3 >= N2:
    print("O numero {} é o maior.E {} é o menor.".format(N3, N1))
elif N1 <= N2 and N1 <= N3 and N3 <= N2:
    print("O numero {} é o maior.E {} é o menor.".format(N2, N1))
elif N1 <= N2 and N3 <= N2 and N3 <= N1:
    print("O numero {} é o maior.E {} é o menor.".format(N2, N3))
elif N1 >= N2 and N3 >= N2 and N3 >= N1:
    print("O numero {} é o maior.E {} é o menor.".format(N3, N2))

