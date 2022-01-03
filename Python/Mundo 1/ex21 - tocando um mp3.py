from pygame import mixer

print(' ====== Exercicio 21 ====== ')
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input()
