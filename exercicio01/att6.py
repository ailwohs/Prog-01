#JULIA
'''6. Faça um programa que leia três notas, calcule e mostre a média aritmética entre elas,
se a media aritmética for:
- Media maior ou igual a 7 - ALUNO APROVADO
- Media menor que 7 - ALUNO REPROVADO'''

nota1=float(input("Digite a primeira nota: \n"))
nota2=float(input("Digite a segunda nota: \n"))
nota3=float(input("Digite a terceira nota: \n"))
media= (nota1 + nota2 + nota3) /3

if media >=7:
    print("ALUNO APROVADO")
else:
    print("ALUNO REPROVADO")    