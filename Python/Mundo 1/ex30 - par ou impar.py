print(' ====== Exercicio 30 ====== ')

num = int(input("Digite um numero inteiro qualquer: "))
ver = num % 2
if ver == 0:
    print("O numero {} é \033[34mPAR\033[m!".format(num))
else:
    print("O numero {} é \033[36mIMPAR\033[m!".format(num))
