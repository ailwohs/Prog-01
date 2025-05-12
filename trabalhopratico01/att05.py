'''5) Faça um algoritmo que solicite 10 números ao usuário. Ao final, o programa deverá exibir na tela:
a) O maior valor digitado
b) O menor valor digitado
c) O somatório dos valores digitados
d) Média dos valores digitados'''

num = int(input("Digite um número: \t> "))
maior_valor = num
menor_valor = num
soma = num

for i in range(9):
    num = int(input("Digite mais um número: \t> "))
    if num > maior_valor:
        maior_valor = num
    if num < menor_valor:
        menor_valor = num
    soma += num

media = soma / 10

print("Maior valor digitado:", maior_valor)
print("Menor valor digitado:", menor_valor)
print("A soma dos números é:", soma)
print("A média dos valores é:", media)