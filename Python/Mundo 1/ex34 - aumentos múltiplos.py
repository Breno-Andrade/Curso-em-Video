print(' ====== Exercicio 34 ====== ')

s = float(input("Digite o salario: "))
if s <= 1250.00:
    ns = s + (s * 15 / 100)
else:
    ns = s + (s * 10 / 100)
print("Quem ganhava \033[31mR${:.2f}\033[m passa a ganhar \033[32mR${:.2f}\033[m".format(s, ns))
