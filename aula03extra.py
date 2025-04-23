# 5 - Preço da mercadoria com desconto
preco = float(input("Digite o preço da mercadoria: "))
desconto = float(input("Digite o percentual de desconto: "))
valor_desconto = preco * desconto / 100
preco_final = preco - valor_desconto
print("Valor do desconto:", valor_desconto)
print("Preço a pagar:", preco_final)

# 6 - Tempo de uma viagem de carro
distancia = float(input("Digite a distância a percorrer (em km): "))
velocidade = float(input("Digite a velocidade média esperada (em km/h): "))
tempo = distancia / velocidade
print("Tempo estimado de viagem (em horas):", tempo)

# 7 - Conversão de Celsius para Fahrenheit
temperatura = int(input("Digite a temperatura em Celsius: "))
fahrenheit = (temperatura * 9 / 5) + 32
print("Temperatura em Fahrenheit:", fahrenheit)

# 8 - Preço de aluguel de carro
km = float(input("Digite a quantidade de km percorridos: "))
dias = int(input("Digite a quantidade de dias de aluguel: "))
preco = (dias * 60) + (km * 0.15)
print("Preço a pagar pelo aluguel do carro:", preco)

# 9 - Redução do tempo de vida de um fumante
cigarros_por_dia = int(input("Quantos cigarros você fuma por dia? "))
anos = int(input("Há quantos anos você fuma? "))
total_cigarros = cigarros_por_dia * 365 * anos
minutos_perdidos = total_cigarros * 10
dias_perdidos = minutos_perdidos / 1440
print("Total de dias de vida perdidos:", dias_perdidos)

# 10 - Tipo de variável e conversões
var = input("Digite um número qualquer: ")
print("Tipo da variável:", type(var))
var = int(var)
print("Tipo da variável após conversão para inteiro:", type(var))
var = float(var)
print("Tipo da variável após conversão para float:", type(var))
var = False
print("Tipo da variável após atribuir False:", type(var))