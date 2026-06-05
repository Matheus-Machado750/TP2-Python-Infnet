"""
Exercício 13

A equipe de desenvolvimento da "Nexus Games" está preparando o lançamento de um novo RPG estratégico, "Arcana Quest".
Para garantir o balanceamento do jogo, eles precisam de uma maneira eficaz de avaliar o desempenho dos jogadores nas fases de teste alfa.
As pontuações obtidas em três cenários cruciais serão utilizadas para calcular um índice de performance final.
O programa em Python, executado em blocos no Deepnote, será essencial para agilizar a avaliação do desempenho dos jogadores, consolidando os resultados e assegurando a precisão dos registros para futuras análises de balanceamento.

Tarefa:

No jogo "Arcana Quest", a pontuação final de um jogador é determinada pela soma das pontuações obtidas em três fases distintas, com a aplicação de um bônus por sincronia tática, uma dedução por gasto excessivo e um fator de amplificação de maestria.
A pontuação base é a soma direta das pontuações das fases de Exploração, Combate e Estratégia. O bônus por sincronia tática é calculado como o dobro da pontuação da Fase de Estratégia, somado à metade (divisão inteira) da pontuação da Fase de Exploração.
A dedução por gasto excessivo corresponde ao triplo do resto da divisão da pontuação da Fase de Combate por 10.
Finalmente, a pontuação resultante (base + bônus - dedução) é multiplicada por um fator de amplificação de maestria, calculado como o quociente da divisão inteira da pontuação da Fase de Exploração por 5, mais 1.

Entrada

O programa receberá três entradas consecutivas. Cada entrada será uma string contendo um número inteiro positivo, representando o poder bruto de uma fase (por exemplo, 15, 20 e 12).
A primeira entrada corresponde à pontuação da Fase de Exploração, a segunda à pontuação da Fase de Combate, e a terceira à pontuação da Fase de Estratégia. Todos os valores fornecidos são válidos para conversão e processamento.

Saída

O programa deve apresentar uma única linha de texto.
Esta linha deve informar a pontuação final calculada de acordo com as regras descritas na tarefa, formatada como: "Pontuação Final em Arcana Quest: XX pontos.", onde XX representa o valor inteiro da pontuação total após todos os cálculos.
"""

valor_exploracao = int(input("Insira poder bruto dessa fase: "))
valor_combate = int(input("Insira poder bruto dessa fase: "))
valor_estrategia = int(input("Insira poder bruto dessa fase: "))

pontuacao_padrao = valor_exploracao + valor_combate + valor_estrategia

bonus_sincronia_tatica = (valor_estrategia * 2) + (valor_exploracao // 2)
gasto_excessivo = (valor_combate % 10) * 3

pontuacao_resultante = (pontuacao_padrao + bonus_sincronia_tatica - gasto_excessivo) * ((valor_exploracao // 5) + 1)

print(f"Pontuação Final em Arcana Quest: {pontuacao_resultante} pontos.")