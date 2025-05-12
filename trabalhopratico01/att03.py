'''3) Elabore um algoritmo que solicite ao usuário um número de 1 a 12. Para cada número, o programa deverá
exibir por extenso o mês correspondente. (ex: Se o usuário digitar 2, deverá escrever “Fevereiro”). Ao digitar
zero, o programa deverá encerrar. Se o usuário digitar algo fora deste escopo, o programa deverá retornar uma
mensagem que foi digitada uma opção incorreta.'''

num=int(input("Digite um número de 1 até 12 \t>"))
while num!=0:
 if num==1:
   print("Janeiro")
 elif num==2:
   print("Fevereiro")
 elif num==3:
   print("Março")
 elif num==4:
   print("Abril")
 elif num==5:
   print("Maio")
 elif num==6:
   print("Junho")
 elif num==7:
   print("Julho")
 elif num==8:
     print("Agosto")
 elif num==9:
    print("Setembro")
 elif num==10:
    print("Outubro")
 elif num==11:
   print("Novembro")
 elif num==12:
  print("Dezembro")
 else:
  print("Opção inválida")
 num=int(input("Digite um número de 1 até 12 ou Zero para encerrar \t>"))