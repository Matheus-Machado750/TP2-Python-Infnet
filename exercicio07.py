"""
Exercício 7

A equipe de Marketing da empresa 'Voz Digital' está desenvolvendo novas campanhas promocionais via SMS para seus clientes.
Para evitar custos adicionais e garantir que todas as mensagens sejam entregues corretamente, é crucial que cada SMS respeite um limite de caracteres.
O gerente de Marketing forneceu o texto de uma mensagem candidata para que seu programa em Python, executado em blocos no Deepnote, verifique se ela atende a essa restrição. O objetivo é assegurar que a comunicação com o cliente seja eficaz e econômica, respeitando as normas das operadoras.

Tarefa:

Com a mensagem de campanha mensagem_candidata = 'Desconto exclusivo para você! Válido por tempo limitado.', o prefixo padrão prefixo_padrao = 'Voz Digital: ' e o sufixo padrão sufixo_padrao = ' Acesse nosso site para detalhes.', você deve calcular o comprimento total da mensagem final, considerando que o prefixo e o sufixo são sempre incluídos.
Além disso, determine quantos caracteres a mensagem_candidata excede ou falta em relação ao espaço disponível, sabendo que o limite total de um SMS é de 160 caracteres.
Guarde as contagens em variáveis (por exemplo, tamanho_total e diferenca_limite) e exiba os valores ao final.
"""

mensagem_candidata = "Desconto exclusivo para você! Válido por tempo limitado."
prefixo_padrao = "Voz Digital: "
sufixo_padrao = " Acesse nosso site para detalhes."

mensagem_completa = prefixo_padrao + mensagem_candidata + sufixo_padrao

tamanho_total = len(mensagem_completa)
tamanho_limite = 160

print(f"O tamanho total da mensagem foi de {tamanho_total} caracteres.")

if tamanho_limite > tamanho_total:

    diferenca_tamanho = tamanho_limite - tamanho_total
    print(f"A mensagem falta {diferenca_tamanho} caracteres para chegar no limite.")

else:

    diferenca_tamanho = tamanho_total - tamanho_limite
    print(f"A mensagem excede {diferenca_tamanho} caracteres em relação ao limite.")