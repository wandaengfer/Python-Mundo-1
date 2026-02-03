#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
n1 = float(input('Digite o primeiro comprimento da reta: '))
n2 = float(input('Digite o segundo comprimento da reta: '))
n3 = float(input('Digite o terceiro comprimento da reta: '))
if n1+n2>n3 and n1+n3>n2 and n2+n3>n1:
    print ('Essas retas formam um triângulo!')
else:
    print('Essas retas não formam um triângulo!')
