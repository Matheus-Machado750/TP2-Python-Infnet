"""
Exercício 4

No contexto de uma disciplina de 'Introdução à Programação com Python', um grupo de educadores busca ferramentas interativas para apoiar o aprendizado dos alunos.
Eles desejam criar um programa simples de pergunta e resposta que ajude os estudantes a compreenderem como a informação é processada após ser fornecida, além de explorar transformações básicas em strings.
Este programa será executado em blocos no ambiente Deepnote, onde os alunos poderão interagir diretamente.
O objetivo é que o programa capture uma mensagem digitada pelo aluno, apresente a mensagem original como confirmação de recebimento e também exiba uma versão da mensagem com a capitalização das letras invertida, reforçando o entendimento sobre manipulação de strings.

Tarefa:

Desenvolva um programa que interaja com o usuário através da captura de uma única informação textual, utilizando mensagem = input() para ler a entrada.

Entrada

O programa receberá uma única linha de texto, representando uma sequência de caracteres fornecida pelo usuário.
Esta entrada pode conter letras maiúsculas, minúsculas, números ou símbolos.

Saída

O programa deve produzir duas linhas de texto:

Uma linha indicando que a mensagem foi recebida com sucesso, seguida do texto original informado pelo usuário.
Uma segunda linha exibindo a mensagem com a capitalização das letras invertida.
"""

mensagem = input("Insira sua mensagem: ")

print(f"Sua mensagem foi recebida com sucesso. Mensagem original: {mensagem}")
print(f"Mensagem formatada: {mensagem.swapcase()}")