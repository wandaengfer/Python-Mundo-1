#Escreva um programa que leia a velocidade de um carro.
#Se ele ultrapassar 80 km/h, mostre uma mensagem dizendo que ele foi multado
#A multa vai custar R$ 7,00 por cada km acima do limite
vel = float(input("Digite a velocidade em km/h: "))
if vel > 80:
    print('Você foi multado')
    print ('Sua multa foi de R$ {:.2f}'.format((vel-80)*7))