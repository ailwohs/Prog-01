'''2) Crie um algoritmo onde o usuário deverá digitar um numeral de 1 a 5 para exibir mensagens, e caso digite 0,
o programa deverá encerrar. Se o usuário digitar algo fora deste escopo, o programa deverá retornar uma
mensagem que foi digitada uma opção incorreta. Para cada número digitado, o programa deverá mostrar o
seguinte:
Número 1: Definição de compilador e interpretador.
Número 2: Cite 5 tipos de dados e o que representa cada um. (Ex: boolean = assume somente dois valores:
true ou false).
Número 3: Definição de typecast e indentação.
Número 4: Definição de Linguagens de Programação com tipagem forte e fraca.
Número 5: Definição de variável e constante. Além disso, informe o que é preciso para declarar uma variável
ou uma constante.
Você deverá escrever o que significa cada um destes itens com suas próprias palavras.'''

num=int(input("Digite um número \t>"))
while num !=0:
 if num == 1:
  print(" a definição de compilador e interpretador é que eles mostram o que a nossa linha de codigos está fazendo de forma mais clara.")
 elif num == 2:
  print("int= mostra um número inteiro / float= coloca um número em decimal / type = mostra o tipo da variavel / boolean = assume somente dois valores que são true ou fals / str = são strings que nada mais são do que sequências (cadeias) de caracteres")
 elif num == 3:
   print("typecast=descobre o tipo de variavel que o programa está usando / identação=escrever conforme as regras do programa")
 elif num == 4:
   print("Linguagem de programação: conjunto de símbolos e códigos usados para dar instruções ao computador / tipagem forte: a linguagem exige que o tipo de dado de um valor seja do mesmo tipo de variável ao qual este valor será atribuído. tipagem fraca: Quando é fraco, não há necessidade de explicitar o tipo de dado, e ele pode mudar conforme o valor que é atribuído a variável.")
 elif num == 5:
   print("A definição de uma variável é que o  valor dela tá sempre mudando e a definição de constante é que o valor permanece sempre o mesmo. / Para declarar uma variável ou uma constante precisamos informar de que tipo a mesma é. ")
 else:
   print("Opção inválida")
 num=int(input("Digite um número ou Zero para encerrar \t>"))