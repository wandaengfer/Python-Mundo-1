#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minúsculas
#Quantas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome
from dataclasses import replace

nome = input('Digite o seu nome completo: ')
MAIS = nome.upper()
minus = nome.lower()
total_letras = len(nome.replace(" ", ''))
primeiro_nome = nome.split()[0]
letras_primeiro = len(nome.split()[0])

print('O seu nome em letras maiúsculas é: {}'.format(MAIS))
print('O seu nome em letras minúsculas é: {}'.format(minus))
print('O seu nome completo tem {} letras'.format(total_letras))
print ('O seu primeiro nome é {} e tem {} letras'.format(primeiro_nome, letras_primeiro))
