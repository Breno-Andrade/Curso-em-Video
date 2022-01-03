print(' ====== Exercicio 35 ====== ')

r1 = float(input("Digite o primeiro valor: "))
r2 = float(input("Digite o segundo valor: "))
r3 = float(input("Digite o terceiro valor: "))

if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("Os valores acima \033[32mPODEM FORMAR\033[m um triângulo!")
else:
    print("Os valores acima \033[31mNÃO PODEM FORMAR\033[m um triângulo!")
