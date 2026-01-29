#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
if n1 > n2 and n1 > n3:
    print ('O primeiro valor é o maior')
if n2 > n1 and n2 > n3:
    print ('O segundo valor é o maior')
if n3 > n1 and n3 > n2:
    print ('O terceiro valor é o maior')
if n1 < n2 and n1 < n3:
    print ('O primeiro valor é o menor')
if n2 < n1 and n2 < n3:
    print ('O segundo valor é o menor')
if n3 < n1 and n3 < n2:
    print ('O terceiro valor é o menor')
