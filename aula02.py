#Exercício 01 - fazer um print com nome e curso em menu

print("""##################################################\n        NOME EM MAIUSCULO \n                REDES DE COMPUTADORES\n ##################################################""")


# Exercício 2 - Faça um programa e declare as variáves x e y. Atribua valores numéricos a essas duas variáveis. Depois faça o seguinte:
#x deve receber o valor dele mesmo elevado ao quadro
#y deve receber o valor dele mesmo dividido por 2
#na sequência, crie as variáveis adicao, subtracao, multiplicacao, divisao_int, divisao_frac, divisao_resto, exponeciacao e atribua a elas o valor correspondente 
# de cada operaçao entre x e y.
#Ao final imprima na tela os resultados. Se você for capaz, imprima tudo com um único comando print, com quebras de linhas.

x = 12  
y = 9
x = x ** 2
y = y / 2

adicao = x + y
subtracao = x - y
multiplicacao = x * y
divisao_int = x // y
divisao_frac = x / y
divisao_resto = x % y
exponenciacao = x ** y

print("Resultados:\n"  "Soma:", adicao, "\n"  "Subtração:", subtracao, "\n"  "Multiplicação:", multiplicacao, "\n"  "Divisão Inteira:", divisao_int, "\n"  "Divisão Fracionária:", divisao_frac, "\n"  "Resto da Divisão:", divisao_resto, "\n""Exponenciação:", exponenciacao)

# Exercício 3 -  Implemente, em um programa em python, a fórmula de Bhaskara: x = -b ± √(b² – 4ac)/ 2. Tente fazer.
#Lembre que a fórmula de Bhaskara resulta dois valores: x1 e x2.

a = 1  
b = -3  
c = 2  

delta = (b ** 2) - (4 * a * c)
x1 = (-b + delta ** 0.5) / (2 * a)
x2 = (-b - delta ** 0.5) / (2 * a)

print("As raízes da equação são: x1 =", x1, "e x2 =", x2)