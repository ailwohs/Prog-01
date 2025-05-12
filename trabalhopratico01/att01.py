'''1. Faça um algoritmo que:
a) leia o valor para a variável HT (horas trabalhadas no mês);
b) leia o valor para a variável VH (valor hora trabalhada):
c) leia o valor para a variável PD (percentual de desconto);
d) Calcule o salário bruto => SB = HT * VH;
e) Calcule o total de desconto => TD = (PD/100)*SB;
f) Calcule o salário líquido => SL = SB - TD;
g) Apresente os valores de: Horas trabalhadas, Salário Bruto, Desconto, Salário Líquido.'''


ht=int(input("Digite a quantidade de horas trabalhadas no mês \n>"))
vh=float(input("Digite o valor da hora trabalhada \n>"))
pd=int(input("Digite o valor de percentual de desconto \n>"))
sb=ht*vh
td=(pd/100)*sb
sl=sb-td
print("horas trabalhadas:",ht, ";valor da hora trabalhada:",vh, ";salário bruto:",sb, ";desconto:",td, ";e o salário liquido:",sl,".")