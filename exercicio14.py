"""
Exercício 14

A equipe de cientistas de dados da ClimaTech opera uma rede de sensores para monitoramento ambiental em larga escala.
Diariamente, eles recebem medições de temperatura em graus Celsius como dados brutos de campo.
Para integrar esses dados em seus relatórios globais e no painel de análise de anomalias no Deepnote, é essencial converter cada leitura para Fahrenheit.
Além da conversão padrão, a equipe precisa calcular um "Indicador de Estabilidade Térmica" que reflete a variabilidade local, sendo este um componente crucial para identificar padrões climáticos atípicos.
O programa Python a ser desenvolvido processará esses valores, garantindo que a análise subsequente seja precisa e consistente.

Tarefa:

Você foi designado a desenvolver um módulo para o sistema de monitoramento climático.
Sua tarefa é processar uma entrada de temperatura em Celsius, convertê-la para Fahrenheit e, simultaneamente, calcular um Indicador de Estabilidade Térmica (IET), que quantifica a dispersão térmica baseada na leitura original.
A precisão e o formato da saída são críticos para a análise automatizada.

Entrada

Uma única linha de texto será fornecida. Esta linha contém um valor numérico que representa a temperatura medida em graus Celsius (por exemplo, 25.0). O valor pode ser positivo, negativo ou zero, e pode conter casas decimais.

Saída

O programa deve produzir uma única linha de texto formatada com as duas métricas calculadas. Primeiramente, o valor da temperatura em Fahrenheit deve ser apresentado, seguido por um ponto e vírgula e um espaço (; ).
A temperatura em Fahrenheit deve ser calculada a partir da temperatura em Celsius utilizando a seguinte fórmula:

F = (Temperatura_Celsius * 9 / 5) + 32

Em seguida, o Indicador de Estabilidade Térmica (IET) deve ser exibido. O IET é calculado pela seguinte fórmula:

IET = (Temperatura_Celsius / 4.0) - (Temperatura_Celsius * 0.08) + 1.5

Ambos os resultados devem ser convertidos para string e concatenados conforme a especificação.
"""

celsius = float(input("Insira o valor em Celsius: "))
F = (celsius * 9 / 5) + 32
IET = (celsius / 4.0) - (celsius * 0.08) + 1.5

F = str(f"{F:.2f}")
IET = str(f"{IET:.2f}")

#print conforme especificação: "Fahrenheit"; "IET"
print(F + "; " + IET)