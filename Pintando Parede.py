#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
#necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m^2
l=float(input('Qual a largura da parede em metros?'))
h=float(input('Qual a altura da parede em metros?'))
print('A quantidade de tinta necessária para pintar a parede é {}l'.format(l*h/2))
