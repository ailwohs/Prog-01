#julia
'''9. Um comerciante comprou um produto e quer vendê-lo com lucro de 45% se o valor da
compra for menor que 20,00; caso contrário, o lucro será de 30%. Ler o valor do produto e
imprimir o valor da venda (conforme as taxas do enunciado).'''

compra=float(input("valor da compra do produto? \n"))

if compra <= 20:
    lucro = compra * 0.45 
else:
    lucro = compra * 0.30
venda = compra + lucro

print("o valor da venda vai ser de : \n", venda)       