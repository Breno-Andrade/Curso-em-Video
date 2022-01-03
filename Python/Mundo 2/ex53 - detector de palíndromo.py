print(' ====== Exercicio 56 ====== ')

frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
juntas = ''.join(palavras)
inverso = ''

# Varrendo a string em ordem inversa, ou seja, do fim para o inicio.
for letra in range(len(juntas) - 1, -1, -1):
    inverso += juntas[letra]
print(inverso)

# Verifica se o conteúdo da string(inverso) é igual a string(juntas) após a inversão.
if inverso == juntas:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo')
