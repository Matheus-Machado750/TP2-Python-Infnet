"""
Exercício 11

No setor de logística da empresa 'Estoque Rápido', o gerente de almoxarifado, Sr. João, precisa monitorar a disponibilidade de produtos.
Para otimizar o controle e evitar rupturas no fornecimento, ele necessita de uma ferramenta ágil que calcule as unidades restantes de um item específico após cada transação de saída.
As informações de estoque inicial e de vendas do dia serão fornecidas manualmente por sua equipe. O objetivo é que um programa em Python, executado em blocos no Deepnote, processe esses valores e apresente o saldo atualizado, permitindo ao Sr. João tomar decisões mais eficientes sobre a reposição.

Tarefa:

Desenvolva um programa para a gestão de inventário que calcule o saldo atual de um item específico após uma transação de débito. O processamento deve considerar a quantidade inicial e a movimentação de saída para determinar o estoque final.

Entrada

A entrada será composta por duas linhas de texto. A primeira linha contém um número inteiro que representa a quantidade total de um determinado produto antes de qualquer movimentação (por exemplo, 100).
A segunda linha contém outro número inteiro que indica o número de unidades que foram retiradas do estoque (por exemplo, 30).
Ambos os valores são fornecidos como sequências de caracteres e sempre corresponderão a números inteiros positivos, onde a quantidade inicial será maior ou igual à quantidade retirada.

Saída

O programa deve produzir uma única linha de texto. Esta linha deve apresentar o total de unidades restantes no estoque, no formato 'Após a retirada de [quantidade_retirada] itens, o saldo atual é de [quantidade_restante] unidades.', onde [quantidade_retirada] corresponde ao valor fornecido na segunda linha da entrada e [quantidade_restante] é o resultado da subtração entre a quantidade inicial e a quantidade retirada.
A formatação deve ser precisa, respeitando os termos indicados.
"""

verificador = 0

while verificador == 0:

    quant_total = int(input("Insira a quantidade total de items no estoque: "))
    quantidade_retirada = int(input("Insira a quantia de items retirados: "))

    quantidade_restante = quant_total - quantidade_retirada

    if quant_total >= quantidade_retirada:
        verificador = 1

print(f"Após a retirada de {quantidade_retirada} itens, o saldo atual é de {quantidade_restante} unidades.")