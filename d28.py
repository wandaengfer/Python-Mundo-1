#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 peça para o usuário tentar
#descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu
from time import sleep
import random
num = int(input('Tente descobrir o número escolhindo pelo computador entre 0 e 5: '))
print ('Analisando o número...')
sleep(2)
escolhido = random.choice([0,1,2,3,4,5])
print('O número escolhido pelo computador foi: {}'.format(escolhido))
if num == escolhido:
    print('Você venceu! :)')
else:
    print('Você perdeu! :(')

