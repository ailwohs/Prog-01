#Julia
# 4. Faça um programa que leia o salário de um funcionário e o percentual de aumento, 
# calcule e mostre o valor do aumento e o novo salário.

salario=float(input("Digite seu salário: \n"))
porcentual=float(input("Digite o porcentual de aumento: \n"))

aumento = salario * (porcentual / 100)
novo_salario = salario + aumento
print("o valor de aumento é de: \n", aumento, "e o novo salário é:", novo_salario)