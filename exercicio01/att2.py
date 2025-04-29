
#Julia
#2. Faça um programa para converter um certo valor em dólar para reais (ver cotação do dia).

cotacao=float(input("Digite o valor do dólar hoje: \n"))
valor=float(input("Quantos deseja converter? \n"))
reais = cotacao * valor
print("o valor de: \n", valor, "em reias fica:", reais)