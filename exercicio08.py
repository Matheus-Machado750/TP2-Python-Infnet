"""
Exercício 8

Uma equipe de eventos está preparando um sistema simples para gerar cartões de boas-vindas em texto (ASCII) para participantes de um workshop.
O cartão deve ter uma borda superior e inferior feitas com o caractere =, e linhas do meio com bordas laterais feitas com = e espaços no conteúdo, seguindo um padrão visual fixo.

Tarefa:

Crie um programa que gere e exiba um cartão semelhante ao do formato abaixo, usando um caractere (no exemplo, "=") e operações de repetição/concatenação.
O cartão deve ser armazenado em uma variável string (por exemplo, cartao) e depois exibido.
O resultado é semelhante a:

==================================
=                                =
=                                =
==================================

"""

caractere_cartao = input("Insira o caractere desejado para compor o cartão: ")
tamanho_cartao = int(input("Insira o tamanho que terá o cartão: "))

linha_horizontal = caractere_cartao * tamanho_cartao
espacos = " " * (tamanho_cartao - 2)

print(f"{linha_horizontal}\n{caractere_cartao + espacos + caractere_cartao}\n{caractere_cartao + espacos + caractere_cartao}\n{linha_horizontal}")