"""
Exercício 3

Um analista de dados em uma empresa de consultoria de marketing precisa organizar seus relatórios de forma mais eficiente.
Os relatórios de performance de campanhas são gerados em formato de texto simples e, para facilitar a leitura e a organização visual, é fundamental existirem separadores claros entre as diferentes seções.
O comprimento desejado para essas linhas de separação, bem como o caractere a ser usado, serão definidos previamente.
Você desenvolverá um pequeno programa em Python, executado em blocos no Deepnote, para automatizar a criação dessas linhas, ajudando o analista a produzir relatórios mais legíveis e profissionais.

Tarefa:

Desenvolva um programa que, a partir de um caractere específico (por exemplo, -) e um comprimento desejado (por exemplo, 30), gere uma linha de separação visual padronizada para relatórios.

Entrada

A entrada consiste em duas informações. A primeira é um caractere único que será utilizado para compor a linha de separação.
A segunda é um número inteiro positivo que representa o comprimento total que a linha de separação deve possuir.
Ambas as informações serão fornecidas ao programa em sequência direta.

Saída

O programa deve produzir uma única linha de texto. Esta linha será formada pela repetição do caractere de entrada, de modo que o seu comprimento total corresponda exatamente ao valor numérico fornecido na entrada.
A saída deve apresentar apenas essa linha gerada.
"""

caractere = input("Insira o caractere desejado: ")
quantidade = int(input("Insira quantas vezes você quer que esse caractere se repita: "))

print(caractere * quantidade)