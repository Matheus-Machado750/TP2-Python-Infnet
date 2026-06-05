"""
Exercício 16

Em um projeto de Engenharia de Software da empresa TechSolutions, a equipe de desenvolvimento precisa criar um sistema robusto de monitoramento.
Para garantir a rastreabilidade e a análise eficiente de eventos, é fundamental que as mensagens de log sejam padronizadas.
O objetivo é construir um programa em Python, a ser executado em blocos no Deepnote, que formate essas mensagens de log.
Este programa permitirá combinar informações essenciais, como um carimbo de tempo (timestamp), o nível de severidade e uma descrição do evento, em uma única linha de texto.
A padronização das mensagens de log é crucial para facilitar a depuração de problemas e a auditoria de sistemas, impactando diretamente a eficiência operacional da empresa.

Tarefa:

Sua tarefa é desenvolver um programa capaz de gerar uma mensagem de log altamente estruturada para auditoria de transações financeiras.
O programa deve receber múltiplas informações sobre uma transação e concatená-las de forma precisa para formar um registro de log unificado.

Entrada

O programa receberá sete strings, uma por linha, que representam os detalhes de uma transação.
A sequência de entrada é: o identificador único da transação (por exemplo, id = 'ABC123'), a data da operação no formato AAAA-MM-DD (por exemplo, data = '2024-01-15'), a hora da operação no formato HH:MM:SS (por exemplo, hora = '14:30:00'), o tipo da operação (e.g., "DEB" para débito, "CRED" para crédito), o número da conta de origem, o número da conta de destino (que pode ser "N/A" se não houver destino específico), e o valor da transação com duas casas decimais.

Saída

O programa deverá produzir uma única linha de texto que constitui o registro de log completo.
Este registro deve iniciar com [LOG: seguido pelo identificador da transação e fechado por ] - DATA: . Em seguida, concatenar a data da operação, um espaço em branco, a hora da operação, o caractere | e a string TIPO: . Prosseguir com o tipo da operação, um espaço em branco, e a seção da transação entre chaves: {ORIGEM: seguida pela conta de origem, a string -> DESTINO: e a conta de destino, fechando com }. Finalmente, adicionar um espaço em branco, VALOR: R$, o valor da transação e um ponto e vírgula ; no final.
"""

id_transacao = input("Inira o identificador único da transação: ")
data = input("Insira a data no formato (AAAA-MM-DD): ")
hora = input("Insira o horário no formato (HH:MM:SS): ")
tipo = input("Insira o tipo da operação ('DEB' para débito, 'CRED' para crédito): ")
numero_conta_origem = input("Insira o número da conta de origem: ")
numero_conta_destino = input("Insira o número da conta de destino (digite 'N/A' cajo não haja destino específico): ")
valor_transacao = float(input("Insira o valor da transação: "))

print(f"[LOG: {id_transacao}] - DATA: {data} {hora} | TIPO: {tipo} {{ORIGEM: {numero_conta_origem} -> {numero_conta_destino}}} VALOR: R${valor_transacao};")