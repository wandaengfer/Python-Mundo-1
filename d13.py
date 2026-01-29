#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento
s=float(input('Digite o salário: R$'))
print('O salário, com 15% de aumento será de R${:.2f}'.format(s+(s*0.15)))