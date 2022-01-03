# Faz uma contagem regressiva de 10 a 0 com uma pausa de 1 segundo.
from time import sleep
print(' ====== Exercicio 46 ====== ')

print('Contagem regresiva para a explosão dos fogos de artificio: ')
for i in range(10, -1, -1):
    print(i)
    sleep(1)
print('🎆🎆🎆')
