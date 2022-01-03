from random import randint
from time import sleep

print(' ====== Exercicio 28 ====== ')

n = randint(0, 5)  # gerando o numero.
print("===" * 20)
print("Eu pensei em um numero entre 0 e 5. Tente advinhar...")
print("===" * 20)
r = int(input("Em qual numero eu pensei: "))  # Usuário tenta adivinhar
print("CARREGANDO...")
sleep(3) # Pausa para o suspense.
if n == r:  # Verifica se os valores são iguais.
    print("\n\033[4;31mPERDI\033[m! eu pensei no numero \033[36m{}\033[m, voce é algum tipo de mago? ".format(n))
else:
    print("\n\033[4;32mGANHEI\033[m! eu pensei no numero \033[36m{}\033[m e não no \033[31m{}\033[m.".format(n, r))
