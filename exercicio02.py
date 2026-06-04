"""
Exercício 2

A equipe de gerenciamento de estoque de uma loja de varejo busca otimizar a criação de códigos de produtos, conhecidos como SKUs (Stock Keeping Units).
Para cada novo item, é necessário gerar um identificador único, combinando um prefixo da categoria do produto e um número de série. Essas informações são fornecidas diretamente no programa para fins de demonstração.
O objetivo é desenvolver um pequeno programa em Python, executado em blocos no Deepnote, que automatize a montagem desses códigos.
Isso garantirá uma organização mais eficiente do inventário e facilitará a rastreabilidade dos produtos na loja.

Tarefa:

O programa deve receber um prefixo de categoria e um número de série como dados, armazenados em variáveis (por exemplo, prefixo = 'ELT' e numero_serie = '12345').
O código SKU completo é construído combinando o prefixo da categoria e, em seguida, o número de série. Ao final, o programa deve exibir o código SKU gerado.
"""

prefixo = input("Insira o prefixo desejado: ")

numero_serie = input("Insira o número de série: ")

codigo_SKU = prefixo + numero_serie

print(codigo_SKU)