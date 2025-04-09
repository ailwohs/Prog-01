# 1 Escreva um programa que peça ao usuário um valor em metros e o exiba convertido em centímetros.

'''metros=float(input("Digite o valor em metros: \n "))
centimetros = metros * 100
print("Metros convertidos para centimetros equivalem a : ", centimetros)'''

# 2 Faça um programa que solicite ao usuário digitar a altura e largura de uma determinada área a ser medida.
#Imprima na tela do valor área total conforme os valores digitados pelo usuário.

'''altura = float(input("Digite a altura da área \n"))
largura = float(input("Digite a largura da área \n"))
area = altura * largura
print("A área total é de ", area)'''

#3 Faça um programa que solicite ao usuário sua idade.
#Depois Imprima esta idade na tela e informe o ano de nascimento do usuário que digitou a idade.

'''idade = int(input("Digite sua idade: \n"))
ano = 2025
ano_nascimento = ano - idade
print("Sua idade é : ", idade, "\t Seu ano de nascimento é:", ano_nascimento)''']

#4 Escreva um programa que peça ao usuário a quantidade de dias, horas, minutos e segundos.
#Calcule o total em segundos.
dias = int(input("Digite os dias \n"))
horas = int(input("Digite as horas \n"))
minutos = int(input("Digite os minutos \n"))
segundos = int(input("Digite os segundos \n"))

total = dias*86400 + horas*3600 + minutos*60 + segundos
print("Total em segundos é: \n", total)


# 5 - Solicite o preço de uma mercadoria e o percentual de desconto.
#Exiba o valor do desconto e o preço apagar.

#6 - Calcule o tempo de uma viagem de carro.
# ao usuário distância a percorrer e a velocidade média esperada para a viagem.

#7 - Converta uma temperatura digitada pelo usuário de Celsius para Fahrenheit. F = (9*C)/5 + 32.

#8 - Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário,
#assim como a quantidade de dias pelos quais o carro foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

#9 - Escreva um programa para calcular a redução do tempo de vida de um fumante.
#Pergunte a quantidadede cigarros fumados por dia e quantos anos ele já fumou.
#Considerando que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá.
#Exiba o total de dias.

#10 - Faça um programa que solicite que o usuário digite um número qualquer e armazena na variavel "var".
#Imprima na tela o tipo de variável "var". Depois converta para inteiro e imprima novamente o tipo de variável.
#Depois converta para float e imprima novamente o tipo de variável.
#Atribua para var o valor "False" e imprima novamente o tipo de variável.