# 1 - Escreva um programa que deverá perguntar três números ao usuário. Imprima estes números em ordem crescente (do menor para o maior)
'''
num1=int(input("Digite o primeiro número \n"))
num2=int(input("Digite o segundo número \n"))
num3=int(input("Digite o terceiro número \n"))

if num1 > num2:
    num1, num2 = num2, num1

if num1 > num3:
    num1, num3 = num3, num1
  
if num2 > num3:
    num2, num3 = num3, num2
   
print("A ordem de forma crescente é: \n", num1, num2, num3)       
        '''


# 2 - Solicite ao usuário que digite um número. Imprima todos os números de 0 até o número digitado pelo usuário.
'''
num=int(input("Digite um número \n"))

for i in range(num+1):
    print(i)
'''
#3 - Faça um algoritmo onde o usuário deverá digitar um número. O programa deverá listar todos os números pares até o número digitado pelo usuário.
'''
num=int(input("Digite um número usuário \n"))
for i in range(num + 1):
    if i % 2 == 0:
        print(i, "é par")
        
'''        

# 4 - Faça um algoritmo que liste todos os números ímpares até 1000. Utilize um laço de repetição que faça incrementos de 3 em 3.
'''
for i in range (0, 1001, 3):
    if i % 2 == 1:
     print(i)
#OBS = NÃO TA CERTA - ARRUMAR OUTRA HORA
'''

# 5 - Faça um programa que solicite dois números ao usuário. Utiliza uma multiplicação por somatória. Ex:o usuário digita 3 e 4. logo, deverá somar 4+4+4.

num1=int(input("Digite o primeiro número \n"))
num2=int(input("Digite o segundo número \n"))

resultado = 0 

for i in range(num1):
    resultado += num2
    
print("O resultado é: \n", resultado)

#imprimir de 100 ate o 0 
'''
for i in range(100, -1, -1):
    print(i)
'''