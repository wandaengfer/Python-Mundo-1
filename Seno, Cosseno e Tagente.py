#Faça um programa que leia um ângulo qualquer e mostre na tela o valor de seno, cosseno e tangente desse ângulo
import math
ang = float(input("Digite o valor do angulo: "))
angrad = math.radians(ang)
print('O seno de {} é {:.2f}'. format(ang, math.sin(angrad)))
print('o cosseno de {} é {:.2f}'. format(ang, math.cos(angrad)))
print('A tangente de {} é {:.2f}'. format(ang, math.tan(angrad)))
