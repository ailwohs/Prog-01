'''8. Faça um programa que leia dois números e efetua a adição. Se o valor somado for
maior que 20, este deverá ser apresentado somando-se a ele 8; se o valor somado for
menor ou igual a 20, este deverá ser apresentado subtraindo-se 5.'''

#JULIA  

num1=float(input("primeiro número: \n"))
num2=float(input("segundo número: \n"))

soma = num1 + num2
if soma > 20:
    resultado = soma + 8
else: 
    resultado = soma - 5
 
print("o valor é: \n", resultado)    
        