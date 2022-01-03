print(' ====== Exercicio 31 ====== ')

km = float(input("Digite a distancia da viagem: "))
if km <= 200:
    valor = km * 0.50
else:
    valor = km * 0.45
print("Voce está prestes de iniciar uma viagem de \033[34m{:.1f}km\033[m.".format(km))
print("E o valor da sua passagem sera de: \033[36mR${:.2f}\033[m".format(valor))