'''5. Faça um programa que leia um número, verifique se este número é positivo, negativo
ou Zero. Se for negativo mostre a mensagem "Você digitou um numero negativo", Se for
positivo mostre:" Você digitou um número positivo e se for zero mostre: “Você digitou
zero”.'''
#Julia
'''
numero=float(input("Digite um número \n"))

if numero > 0:
    print("Você digitou um número positivo.")
else:
    if numero < 0:
        print("Você digitou um número negativo.")
    else:
        print("Você digitou zero.")
'''


numero=float(input("Digite um número \n"))

if numero > 0:
    print("Você digitou um número positivo.")

elif numero < 0:
        print("Você digitou um número negativo.")
else:
        print("Você digitou zero.")