print(' ====== Exercício 11 ====== ')
# Solicitando os valores de largura e altura para o usuário.
lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
# Calculando a area da parede.
area = alt * lar
# Calculando a quantidade de tinta necessária para pintar a parede.
tin = area / 2
# Exibindo o resultado para o usuário.
print('Sua parede tem a dimensão de {}x{} e sua area é de {}m².'.format(lar, alt, area))
print('Para pintar sua parede, você precisará de {}l de tinta.'.format(tin))
