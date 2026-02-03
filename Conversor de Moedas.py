#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#Considere: US$1.00=R$3.27
n=float(input('Quantos reais você tem? R$'))
print('Você pode comprar US${:.2f}'.format(n/3.27))
