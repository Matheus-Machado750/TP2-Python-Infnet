"""
Exercício 15

Uma equipe de comunicação digital está analisando a qualidade textual das mensagens enviadas em campanhas de marketing.
Um dos indicadores utilizados é a porcentagem de vogais em relação ao total de caracteres da mensagem, considerando que textos muito pobres em vogais podem indicar erros de digitação ou baixa legibilidade.
Para essa análise, todos os caracteres devem ser considerados no total, incluindo letras, espaços e sinais de pontuação.
Um programa em Python, executado em blocos no Deepnote, será utilizado para realizar esse cálculo de forma automática e padronizada.

Tarefa:

Desenvolva um programa que calcule a porcentagem de vogais presentes em uma mensagem inserida pelo usuário, em relação ao número total de caracteres da string.
O programa deve conter comentários explicando as principais etapas do código.
Atenção, considere todas as vogais, independentemente de serem maiúsculas ou minúsculas.

Entrada

O texto a ser analisado é a string definida na variável mensagem, recebida do usuário.

Saída

O programa deve produzir uma única linha de texto exibindo a porcentagem de vogais em relação ao total de caracteres da mensagem.
"""

mensagem = input("Insira sua mensagem: ").lower()

vogais = ["a", "e", "i", "o", "u"]

contador = 0

for i in mensagem:

    if i in vogais:
        contador += 1

porcentagem = contador / len(mensagem) * 100

print(f"{porcentagem:.2f}% da mensagem é composta por vogais")