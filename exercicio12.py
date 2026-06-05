"""
Exercício 12

Na loja 'Preço Bom', o gerente de vendas precisa calcular o valor total de produtos para seus clientes quando eles optam por parcelamentos com juros.
Para garantir transparência, o cálculo deve incluir juros simples aplicados sobre o preço à vista, além de uma taxa administrativa que incide sobre o montante financiado.
As informações de preço, taxa de juros mensal, número de parcelas e taxa administrativa são fornecidas diretamente pelos clientes.
Um programa em Python executado em blocos no Deepnote auxiliará o gerente a determinar o valor final e o valor de cada parcela, garantindo que os clientes compreendam o custo total de sua compra.

Tarefa:

Um sistema de cálculo financeiro necessita determinar o valor total final e o valor de cada parcela mensal para um produto, considerando o preço à vista, uma taxa de juros simples mensal e uma taxa administrativa percentual aplicada sobre o montante financiado após os juros.

Entrada

As informações são fornecidas sequencialmente, uma por linha, por meio de input().
A primeira linha contém um valor numérico representando o preço à vista do produto (por exemplo, preco = 1500.00).
A segunda linha apresenta a taxa de juros mensal simples, expressa como um decimal (por exemplo, taxa_juros = 0.02 para 2 % ao mês).
A terceira linha indica o número total de meses para o pagamento, como um número inteiro (por exemplo, meses = 12).
A quarta e última linha contém a taxa administrativa percentual única, também como um decimal (por exemplo, taxa_admin = 0.05 para 5 %), que incide apenas sobre o valor final, já com juros.

Fórmula de juros simples

valor_com_juros = valor_inicial * (1 + taxa_juros * meses)

Saída

O programa deve produzir duas linhas de saída.
A primeira linha exibirá o valor total final a ser pago pelo produto, incluindo juros e a taxa administrativa, formatado com duas casas decimais.
A segunda linha deverá apresentar o valor de cada parcela mensal, igualmente formatado com duas casas decimais, ambos como uma string.
"""

preco = float(input("Insira o preço: "))
taxa_juros = float(input("Insira a taxa de juros mensais: "))
meses = int(input("Por quantos meses a compra foi parcelada ? "))
taxa_admin = float(input("Insira a taxa de administração: "))

valor_com_juros = preco * (1 + taxa_juros * meses)

valor_admin = taxa_admin * valor_com_juros

valor_final = valor_com_juros + valor_admin

print(f"O valor final foi de : R${valor_final:.2f}")
print(f"O valor de cada parcela é de {valor_final / meses:.2f}")