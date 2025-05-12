'''4) Construa um algoritmo onde o usuário informará numericamente o dia, o mês e o ano de uma determinada
data e o programa informará se aquela é uma data válida. Considere que os meses 1,3,5,7,8,10 e 12 poderão
ter no máximo 31 dias; os meses 4, 6, 9 e 11 poderão ter no máximo 30 dias e o mês 2 tem no máximo 28 dias.
Se a data estiver correta, imprimir no formato dd/mm/AAAA. Se a data for inválida, imprima na tela “Data
Inválida”.'''

while 1==1:
    d=int(input("Digite o dia \t>"))
    m=int(input("Digite o mês \t>"))
    a=int(input("Digite o ano \t>"))
    if (d >=32):
        print("Dia Inválido")
        break
    elif (m >=13):
        print("Mês Inválido")
        break
    elif (d >28 and m == 2):
        print("Data Inválida")
        break
    elif (d <=31 and (m == 4 or m == 6 or m == 9 or m == 11)):  
        print ("Data valida", d,"/" ,m,"/",a,)
        break
    elif (d <=31 and (m == 1 or m == 2 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12)):  
        print("Data valida", d,"/" ,m,"/",a,)
    else:
        print("Data Inválida")
