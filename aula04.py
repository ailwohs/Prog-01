numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
if numero1 > numero2:
    print("O maior número é:", numero1)
elif numero2 > numero1:
    print("O maior número é:", numero2)
else:
    print("Os dois números são iguais.")


##################################################

numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")


#####################################################

resposta = input("Você deseja prosseguir? (sim/não): ")
if resposta == "sim":
    print("Bem-vindo!")
else:
    print("Até a próxima!")



 #######################################################
 # # Programa em Python para verificar se o número é maior ou menor que 5


num = int(input("Digite um número de 0 a 10: "))

if 0 <= num <= 10:
    if num > 5:
        print("O número é maior que 5")
    if num < 5:
        print("O número é menor que 5")
    else:
        print("O número é igual a 5")
else:
    print("Número fora do intervalo permitido")
   

