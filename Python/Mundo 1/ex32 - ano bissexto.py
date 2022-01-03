from datetime import date

print(' ====== Exercicio 32 ====== ')

ano = int(input("Digite o ano para saber se é ou não bissexto: "))
# Se o usuário digitar 0, o programa utilizara a data atual por meio do modulo datetime.
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} \033[32mÉ BISSEXTO\033[m!".format(ano))
else:
    print("O ano  {} \033[31mNÃO É BISSEXTO\033[m!".format(ano))